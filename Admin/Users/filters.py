import django_filters
from Admin.utils.filters.fields import IsActiveField
from core.User.models import User


class UserFilter(django_filters.FilterSet):
    is_active = IsActiveField(required=False)

    class Meta:
        model = User
        fields = ('is_active',)
