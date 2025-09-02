import django_tables2 as tables

from Admin.utils.tables import fields as custom_fields
from core.Currency.models import Currency


class CurrencyTable(tables.Table):
    id = custom_fields.HrefColumn(reverse_url='handbooks:currency-view')
    is_active = tables.BooleanColumn()
    actions = custom_fields.DefaultActionFields(base_url='handbooks:currency')

    class Meta:
        model = Currency
        template_name = "Admin/base/tables/components/table_template.html"
        fields = ('id', 'name', 'code', 'symbol', 'is_active')
        ordering_fields = ('id', 'name', 'code')
