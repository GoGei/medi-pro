import django_filters
from Admin.utils.filters.fields import IsActiveMixinField
from core.User.models import User


class TimezoneHandbookFilter(django_filters.FilterSet):
    is_active = IsActiveMixinField(required=False)

    class Meta:
        model = User
        fields = ('is_active',)
