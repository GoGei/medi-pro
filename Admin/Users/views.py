from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext_lazy as _
from Admin.utils.tables.handler import TableHandler
from core.User.models import User
from .tables import UsersTable
from .filters import UserFilter


@login_required
def user_list(request):
    handler = TableHandler(
        session_key='users_table',
        request=request,
        queryset=User.objects.users(),
        table_class=UsersTable,
        filterset_class=UserFilter,
    )
    content, filterset = handler.process()
    table = {
        'content': content,
        'filterset': filterset,
        'title': _('Users list'),
    }
    return render(request, 'Admin/Users/list.html', {'table': table})


@login_required
def user_view(request, user_id):
    user: User = get_object_or_404(User.objects.users(), pk=user_id)
    return render(request, 'Admin/Users/view.html', {'user': user})
