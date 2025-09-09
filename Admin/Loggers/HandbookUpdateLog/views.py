from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

from Admin.utils.tables.handler import TableHandler
from core.Loggers.models import HandbookUpdateLog
from .tables import HandbookUpdateLogTable
from .filters import HandbookUpdateLogFilter


@login_required
def handbooks_update_list(request):
    handler = TableHandler(
        session_key='handbooks_update_table',
        request=request,
        queryset=HandbookUpdateLog.objects.select_related('user'),
        table_class=HandbookUpdateLogTable,
        filterset_class=HandbookUpdateLogFilter,
        default_ordering=('-stamp',),
        search_fields=('^user__email', '^user__first_name', '^user__last_name')
    )
    handler = handler.process()
    table = {
        'handler': handler,
        'title': _('Handbooks updates list'),
    }
    return render(request, 'Admin/Loggers/HandbookUpdateLog/list.html', {'table': table})
