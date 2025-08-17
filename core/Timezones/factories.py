from django.utils import timezone

from factory import LazyAttribute, fuzzy
from factory.django import DjangoModelFactory
from zoneinfo import available_timezones, ZoneInfo

from .models import TimezoneHandbook


def get_offset_from_tz(tz_name):
    tz = timezone.now().astimezone(ZoneInfo(tz_name))
    return tz.strftime('%z')


class TimezoneHandbookFactory(DjangoModelFactory):
    name = fuzzy.FuzzyChoice(available_timezones())
    offset = LazyAttribute(lambda x: get_offset_from_tz(x.name))
    label = LazyAttribute(lambda x: x.name.replace('_', ' ').capitalize())

    class Meta:
        model = TimezoneHandbook
        django_get_or_create = ('name',)
