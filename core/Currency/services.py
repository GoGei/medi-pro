import json
from collections import Counter

from django.db.models import QuerySet
from django.db.transaction import atomic
from django.utils.translation import gettext_lazy as _

from .const import DEFAULT_FIXTURE
from .models import Currency


class LoadCurrenciesException(Exception):
    pass


def run_validations(data: list[dict]):
    code_list: list[str] = [x['code'] for x in data]
    duplicated = [item for item, count in Counter(code_list).items() if count > 1]
    if duplicated:
        msg = _('Duplicated codes presented: {duplicated}').format(duplicated=', '.join(duplicated))
        raise LoadCurrenciesException(msg)


@atomic
def import_currencies_from_fixture(archive_not_mentioned: bool = True, fixture: str = DEFAULT_FIXTURE,
                                   data: list[dict] = None) -> QuerySet[Currency]:
    mentioned: set[int] = set()
    if not data:
        data = json.load(open(fixture, 'r'))

    for item in data:
        obj, _ = Currency.objects.update_or_create(
            code=item['code'],
            defaults={
                'name': item['name'],
                # 'symbol_native': item['symbol_native'],
                'symbol': item['symbol'],
            }
        )
        mentioned.add(obj.id)
        if not obj.is_active:
            obj.restore()

    if archive_not_mentioned:
        Currency.objects.exclude(id__in=mentioned).archive()
    return Currency.objects.filter(id__in=mentioned)
