import django_tables2 as tables

from Admin.utils.tables import fields as custom_fields
from core.Medicine.models import PatientRelation


class PatientRelationTable(tables.Table):
    id = custom_fields.HrefColumn(reverse_url='medicine:patient-relations-view')
    is_active = tables.BooleanColumn()
    actions = custom_fields.DefaultActionFields(base_url='medicine:patient-relations', view_only=True)

    class Meta:
        model = PatientRelation
        template_name = "Admin/base/tables/components/table_template.html"
        fields = ('id', 'name', 'is_active')
        ordering_fields = ('id', 'name',)
