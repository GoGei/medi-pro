from django import forms
from django.utils.translation import gettext_lazy as _
from Admin.utils.forms.base import BaseModelForm
from core.Employee.models import EmployeeRole


class EmployeeRoleForm(BaseModelForm):
    name = forms.CharField(label=_('Name'), max_length=EmployeeRole.name.field.max_length)

    class Meta:
        model = EmployeeRole
        fields = ('name',)
