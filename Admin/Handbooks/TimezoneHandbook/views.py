from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from django.utils.translation import gettext_lazy as _
from Admin.utils.tables.handler import TableHandler
from core.Timezones.models import TimezoneHandbook
from .tables import TimezoneHandbookTable
from .filters import TimezoneHandbookFilter


@login_required
def timezone_list(request):
    handler = TableHandler(
        session_key='timezones_table',
        request=request,
        queryset=TimezoneHandbook.objects.all(),
        table_class=TimezoneHandbookTable,
        filterset_class=TimezoneHandbookFilter,
        search_fields=('name',)
    )
    handler = handler.process()
    table = {
        'handler': handler,
        'title': _('Timezones handbooks list'),
    }
    return render(request, 'Admin/Handbooks/TimezoneHandbooks/list.html', {'table': table})


@login_required
def timezone_view(request, timezone_id):
    timezone: TimezoneHandbook = get_object_or_404(TimezoneHandbook, pk=timezone_id)
    return render(request, 'Admin/Handbooks/TimezoneHandbooks/view.html', {'timezone': timezone})
