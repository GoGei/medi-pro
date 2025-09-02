import json
from .const import DEFAULT_FIXTURE
from .models import Currency


def import_currencies_from_fixture(archive_not_mentioned: bool = True, fixture: str = DEFAULT_FIXTURE):
    mentioned: set[int] = set()
    data = json.load(open(fixture, 'r'))

    for item in data:
        obj, _ = Currency.objects.update_or_create(
            code=item['code'],
            defaults={
                'name': item['name'],
                'symbol': item['symbol_native'],
            }
        )
        mentioned.add(obj.id)
        if not obj.is_active:
            obj.restore()

    if archive_not_mentioned:
        Currency.objects.exclude(id__in=mentioned).archive()
