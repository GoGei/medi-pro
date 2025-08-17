import django_tables2 as tables

from Admin.utils.tables import fields as custom_fields
from django.utils.translation import gettext_lazy as _
from core.Timezones.models import TimezoneHandbook


class TimezoneHandbookTable(tables.Table):
    id = custom_fields.HrefColumn(
        reverse_url='handbooks:timezones-view',
        verbose_name=_('ID'),
        orderable=True
    )
    is_active = tables.BooleanColumn()
    actions = tables.TemplateColumn(
        template_name='Admin/Handbooks/TimezoneHandbooks/table_actions_column.html',
        verbose_name=_('Actions'),
        orderable=False
    )

    class Meta:
        model = TimezoneHandbook
        template_name = "Admin/base/tables/components/table_template.html"
        fields = ('id', 'name', 'offset', 'label', 'is_active')
        ordering_fields = ('id', 'name')
