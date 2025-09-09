import django_tables2 as tables

from Admin.utils.tables import fields as custom_fields
from core.Employee.models import EmployeeRole


class EmployeeRoleTable(tables.Table):
    id = custom_fields.HrefColumn(reverse_url='clinic-settings:employee-color-view')
    is_active = tables.BooleanColumn()
    actions = custom_fields.DefaultActionFields(
        view_only=True,
        base_url='clinic-settings:employee-role',
        extra_context={
            'edit_url': 'clinic-settings:employee-role-edit',  # set edit explicitly
        })

    class Meta:
        model = EmployeeRole
        template_name = "Admin/base/tables/components/table_template.html"
        fields = ('id', 'name', 'slug', 'is_active', 'actions')
        ordering_fields = ('id', 'name')
