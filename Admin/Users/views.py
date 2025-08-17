from django.shortcuts import render
from core.User.models import User
from .tables import UsersTable
from .filters import UserFilter
from Admin.utils.tables.handler import TableHandler


def customer_list(request):
    handler = TableHandler(
        request=request,
        queryset=User.objects.users(),
        table_class=UsersTable,
        filterset_class=UserFilter,
    )
    table, filterset = handler.process()
    return render(request, "Admin/Users/list.html", {"table": table, "filter": filterset})
