import django_tables2 as tables
from Admin.utils.tables import fields as custom_fields
from core.User.models import User


class AdminsTable(tables.Table):
    id = custom_fields.HrefColumn(reverse_url='admins-view')
    actions = custom_fields.DefaultActionFields(base_url='admins')

    class Meta:
        model = User
        template_name = "Admin/base/tables/components/table_template.html"
        fields = ('id', 'email', 'is_staff', 'is_superuser', 'is_active', 'first_name', 'last_name', 'actions')
        ordering_fields = ('id', 'first_name')
