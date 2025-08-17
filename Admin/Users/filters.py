from core.User.models import User

from Admin.utils.tables.filters import SearchFilter


class UserFilter(SearchFilter):
    class Meta:
        model = User
        fields = ('is_active', 'search')
        search_fields = ('^email', '=phone_number', 'first_name', 'last_name')
