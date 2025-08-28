import django_tables2 as tables

from Admin.utils.tables import fields as custom_fields
from django.utils.translation import gettext_lazy as _
from core.Country.models import Country


class CountryTable(tables.Table):
    id = custom_fields.HrefColumn(reverse_url='handbooks:country-view')
    is_active = tables.BooleanColumn()
    actions = custom_fields.DefaultActionFields(base_url='handbooks:country')

    class Meta:
        model = Country
        template_name = "Admin/base/tables/components/table_template.html"
        fields = ('id', 'name', 'cca2', 'ccn3', 'is_active')
        ordering_fields = ('id', 'name', 'cca2', 'ccn3')
