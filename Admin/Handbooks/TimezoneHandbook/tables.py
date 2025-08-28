import django_tables2 as tables

from Admin.utils.tables import fields as custom_fields
from core.Timezones.models import TimezoneHandbook


class TimezoneHandbookTable(tables.Table):
    id = custom_fields.HrefColumn(reverse_url='handbooks:timezones-view')
    is_active = tables.BooleanColumn()
    actions = custom_fields.DefaultActionFields(base_url='handbooks:timezones')

    class Meta:
        model = TimezoneHandbook
        template_name = "Admin/base/tables/components/table_template.html"
        fields = ('id', 'name', 'offset', 'label', 'is_active')
        ordering_fields = ('id', 'name')
