import django_tables2 as tables
from django.utils.translation import gettext_lazy as _

from Admin.utils.tables import fields as custom_fields
from core.Loggers.models import HandbookUpdateLog


class HandbookUpdateLogTable(tables.Table):
    handbook = tables.Column(orderable=False, accessor='get_handbook_display')
    user = custom_fields.HrefColumn(verbose_name=_('Users'),
                                    reverse_url='users-view',
                                    reverse_field='user_id',
                                    record_label='user')

    class Meta:
        model = HandbookUpdateLog
        template_name = "Admin/base/tables/components/table_template.html"
        fields = ('id', 'handbook', 'user', 'stamp')
        ordering_fields = ('stamp',)
