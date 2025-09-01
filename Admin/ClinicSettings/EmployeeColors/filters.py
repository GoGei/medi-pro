import django_filters
from django.utils.translation import gettext_lazy as _
from Admin.utils.filters.fields import IsActiveMixinField, IsActiveField
from core.Colors.models import EmployeeColors


class EmployeeColorsFilter(django_filters.FilterSet):
    is_active = IsActiveMixinField(required=False)
    is_default = IsActiveField(required=False, choices=(
        ('', '---------'),
        ('true', _('Default')),
        ('false', _('Not default')),
    ))

    class Meta:
        model = EmployeeColors
        fields = ('is_active',)
