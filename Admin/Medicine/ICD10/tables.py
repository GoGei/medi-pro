import django_tables2 as tables

from Admin.utils.tables import fields as custom_fields
from django.utils.translation import gettext_lazy as _
from core.Medicine.models import ICD10


class ICD10Table(tables.Table):
    id = custom_fields.HrefColumn(
        reverse_url='medicine:icd10-view',
        verbose_name=_('ID'),
        orderable=True
    )
    is_active = tables.BooleanColumn()
    actions = tables.TemplateColumn(
        template_name='Admin/Medicine/ICD10/table_actions_column.html',
        verbose_name=_('Actions'),
        orderable=False
    )

    class Meta:
        model = ICD10
        template_name = "Admin/base/tables/components/table_template.html"
        fields = ('id', 'name', 'code', 'source', 'is_active')
        ordering_fields = ('id', 'name', 'code')
