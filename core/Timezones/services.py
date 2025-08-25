from zoneinfo import available_timezones, ZoneInfo

from django.db import transaction
from django.db.models import QuerySet
from django.utils import timezone
from .models import TimezoneHandbook


def import_timezones(archive_not_mentioned: bool = True):
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


@transaction.atomic
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
