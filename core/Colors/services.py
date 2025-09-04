import json

from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db.models import QuerySet
from django.utils.translation import gettext_lazy as _
from django.db.transaction import atomic

from .const import DEFAULT_FIXTURE
from .models import EmployeeColors

regex = r'#[0-9a-fA-F]{6}'
color_regex = RegexValidator(regex=regex)


class LocaColorsException(Exception):
    pass


def run_validator(item: dict):
    item['sideline'] = item['sideline'].upper()
    item['background'] = item['background'].upper()

    try:
        color_regex(item['sideline'])
    except ValidationError:
        msg = _('Sideline {sideline} does not match regex: {regex}').format(regex=regex, sideline=item['sideline'])
        raise LocaColorsException(msg)

    try:
        color_regex(item['background'])
    except ValidationError:
        msg = _('Background {background} does not match regex: {regex}').format(regex=regex,
                                                                                background=item['background'])
        raise LocaColorsException(msg)


@atomic
def import_colors_from_fixture(archive_not_mentioned: bool = True, fixture: str = DEFAULT_FIXTURE,
                               data: list[dict] = None) -> QuerySet[EmployeeColors]:
    mentioned: set[int] = set()
    if not data:
        data = json.load(open(fixture, 'r'))

    for item in data:
        run_validator(item=item)

        base_field = item.pop('sideline')
        obj, created = EmployeeColors.objects.update_or_create(
            sideline=base_field,
            defaults=item
        )
        mentioned.add(obj.id)
        if not obj.is_active:
            obj.restore()

    if archive_not_mentioned:
        EmployeeColors.objects.exclude(id__in=mentioned).archive()
    if EmployeeColors.objects.active().filter(is_default=True).count() > 1:
        raise LocaColorsException(_('After import there are more than 1 default color'))
    return EmployeeColors.objects.filter(id__in=mentioned)
