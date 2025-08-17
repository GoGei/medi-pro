import django_tables2 as tables

from Admin.utils.tables import fields as custom_fields
from django.utils.translation import gettext_lazy as _
from core.User.models import User


class UsersTable(tables.Table):
    id = custom_fields.HrefColumn(
        reverse_url='users-view',
        verbose_name=_('ID'),
        orderable=True
    )
    actions = tables.TemplateColumn(
        template_name='Admin/Users/table_actions_column.html',
        verbose_name=_('Actions'),
        orderable=False
    )

    class Meta:
        model = User
        template_name = "Admin/base/tables/components/table_template.html"
        fields = ('id', 'email', 'full_name', 'is_active')
        ordering_fields = ('id', 'email')
