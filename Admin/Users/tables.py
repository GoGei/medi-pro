import django_tables2 as tables

from Admin.utils.tables import fields as custom_fields
from core.User.models import User


class UsersTable(tables.Table):
    id = custom_fields.HrefColumn(reverse_url='users-view')
    actions = custom_fields.DefaultActionFields(base_url='users', view_only=True)

    class Meta:
        model = User
        template_name = "Admin/base/tables/components/table_template.html"
        fields = ('id', 'email', 'full_name', 'is_active')
        ordering_fields = ('id', 'email')
