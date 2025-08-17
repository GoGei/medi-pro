import django_filters
from Admin.utils.filters.fields import IsActiveMixinField
from core.Timezones.models import TimezoneHandbook


class TimezoneHandbookFilter(django_filters.FilterSet):
    is_active = IsActiveMixinField(required=False)

    class Meta:
        model = TimezoneHandbook
        fields = ('is_active',)
