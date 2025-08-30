import django_tables2 as tables

from Admin.utils.tables import fields as custom_fields
from core.Medicine.models import AllergyType


class AllergyTypeTable(tables.Table):
    id = custom_fields.HrefColumn(reverse_url='medicine:allergy-types-view')
    is_active = tables.BooleanColumn()
    actions = custom_fields.DefaultActionFields(base_url='medicine:allergy-types', view_only=True)

    class Meta:
        model = AllergyType
        template_name = "Admin/base/tables/components/table_template.html"
        fields = ('id', 'name', 'code', 'source', 'is_active')
        ordering_fields = ('id', 'name', 'code')
