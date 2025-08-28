import django_tables2 as tables

from Admin.utils.tables import fields as custom_fields
from django.utils.translation import gettext_lazy as _
from core.Medicine.models import ICD10


class ICD10Table(tables.Table):
    id = custom_fields.HrefColumn(reverse_url='medicine:icd10-view')
    is_active = tables.BooleanColumn()
    actions = custom_fields.DefaultActionFields(base_url='medicine:icd10', view_only=True)

    class Meta:
        model = ICD10
        template_name = "Admin/base/tables/components/table_template.html"
        fields = ('id', 'name', 'code', 'source', 'is_active')
        ordering_fields = ('id', 'name', 'code')
