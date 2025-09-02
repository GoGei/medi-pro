import django_tables2 as tables

from Admin.utils.tables import fields as custom_fields
from core.Colors.models import EmployeeColors

template = '<span class="label" style="background-color: {{ record.%s }}; color: #fff;">{{ record.%s }}</span>'


class EmployeeColorsTable(tables.Table):
    id = custom_fields.HrefColumn(reverse_url='clinic-settings:employee-color-view')
    sideline = tables.TemplateColumn(template_code=template % ('sideline', 'sideline'))
    background = tables.TemplateColumn(template_code=template % ('background', 'background'))
    is_default = tables.BooleanColumn()
    is_active = tables.BooleanColumn()
    actions = custom_fields.DefaultActionFields(
        base_url='clinic-settings:employee-color',
        template_name='Admin/ClinicSettings/EmployeeColors/actions_template.html')

    class Meta:
        model = EmployeeColors
        template_name = "Admin/base/tables/components/table_template.html"
        fields = ('id', 'name', 'sideline', 'background', 'is_default', 'is_active', 'actions')
        ordering_fields = ('id', 'name')
