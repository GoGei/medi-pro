from zoneinfo import available_timezones, ZoneInfo
from django.utils import timezone
from .models import TimezoneHandbook


def import_timezones():
    for tz_name in sorted(available_timezones()):
        dt = timezone.now().astimezone(ZoneInfo(tz_name))
        offset_td = dt.utcoffset()
        hours, minutes = divmod(offset_td.total_seconds() // 60, 60)
        sign = '+' if hours >= 0 else '-'
        offset = f"{sign}{abs(int(hours)):02d}:{int(minutes):02d}"

        TimezoneHandbook.objects.update_or_create(
            name=tz_name,
            defaults={
                'offset': offset,
                'label': tz_name.replace('_', ' '),
            }
        )
