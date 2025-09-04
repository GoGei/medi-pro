from zoneinfo import available_timezones, ZoneInfo
from collections import Counter

from django.db.models import QuerySet
from django.db.transaction import atomic
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .models import TimezoneHandbook


def import_timezones(archive_not_mentioned: bool = True) -> QuerySet[TimezoneHandbook]:
    mentioned: set[int] = set()
    for tz_name in sorted(available_timezones()):
        dt = timezone.now().astimezone(ZoneInfo(tz_name))
        offset_td = dt.utcoffset()
        hours, minutes = divmod(offset_td.total_seconds() // 60, 60)
        sign = '+' if hours >= 0 else '-'
        offset = f"{sign}{abs(int(hours)):02d}:{int(minutes):02d}"

        obj, _ = TimezoneHandbook.objects.update_or_create(
            name=tz_name,
            defaults={
                'offset': offset,
                'label': tz_name.replace('_', ' '),
            }
        )
        mentioned.add(obj.id)
        if not obj.is_active:
            obj.restore()

    if archive_not_mentioned:
        TimezoneHandbook.objects.exclude(id__in=mentioned).archive()
    return TimezoneHandbook.objects.filter(id__in=mentioned)


class LoadTimezonesException(Exception):
    pass


def run_validations(data: list[dict]):
    name_list: list[str] = [x['name'] for x in data]
    duplicated = [item for item, count in Counter(name_list).items() if count > 1]
    if duplicated:
        msg = _('Duplicated names presented: {duplicated}').format(duplicated=', '.join(duplicated))
        raise LoadTimezonesException(msg)


@atomic
def load_timezones(data: list[dict], archive_not_mentioned: bool = True) -> QuerySet[TimezoneHandbook]:
    mentioned: set[int] = set()

    for item in data:
        obj, _ = TimezoneHandbook.objects.update_or_create(
            name=item['name'],
            defaults={
                'offset': item['offset'],
                'label': item['label'],
            }
        )
        mentioned.add(obj.id)
        if not obj.is_active:
            obj.restore()

    if archive_not_mentioned:
        TimezoneHandbook.objects.exclude(id__in=mentioned).archive()

    return TimezoneHandbook.objects.filter(id__in=mentioned)
