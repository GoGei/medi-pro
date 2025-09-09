import django_filters
from Admin.utils.filters.fields import IsActiveMixinField
from core.Employee.models import EmployeeRole


class EmployeeRoleFilter(django_filters.FilterSet):
    is_active = IsActiveMixinField(required=False)

    class Meta:
        model = EmployeeRole
        fields = ('is_active',)
