import django_tables2 as tables

from Admin.utils.tables import fields as custom_fields
from django.utils.translation import gettext_lazy as _
from core.Medicine.models import PatientRelation


class PatientRelationTable(tables.Table):
    id = custom_fields.HrefColumn(
        reverse_url='medicine:patient-relations-view',
        verbose_name=_('ID'),
        orderable=True
    )
    is_active = tables.BooleanColumn()
    actions = tables.TemplateColumn(
        template_name='Admin/Medicine/PatientRelation/table_actions_column.html',
        verbose_name=_('Actions'),
        orderable=False
    )

    class Meta:
        model = PatientRelation
        template_name = "Admin/base/tables/components/table_template.html"
        fields = ('id', 'name', 'is_active')
        ordering_fields = ('id', 'name',)
