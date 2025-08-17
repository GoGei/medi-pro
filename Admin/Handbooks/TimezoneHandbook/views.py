from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django_hosts import reverse

from Admin.utils.tables.handler import TableHandler
from core.Timezones.models import TimezoneHandbook
from .tables import TimezoneHandbookTable
from .forms import TimezoneHandbookEditForm
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


@login_required
def timezone_edit(request, timezone_id):
    timezone: TimezoneHandbook = get_object_or_404(TimezoneHandbook, pk=timezone_id)
    if request.POST.get('cancel'):
        return redirect(reverse('handbooks:timezones-view', args=[timezone.id], host='admin'))

    form_body = TimezoneHandbookEditForm(request.POST or None, request.FILES or None, request=request,
                                         instance=timezone)
    if form_body.is_valid():
        timezone = form_body.save_on_edit()
        return redirect(reverse('handbooks:timezones-view', args=[timezone.id], host='admin'))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/Handbooks/TimezoneHandbooks/edit.html', {'timezone': timezone, 'form': form})


@login_required
def timezone_archive(request, timezone_id):
    timezone: TimezoneHandbook = get_object_or_404(TimezoneHandbook, pk=timezone_id)
    timezone.archive(request.user)
    messages.success(request, _('Timezone successfully archived!'))
    return redirect(reverse('handbooks:timezones-list', host='admin'))


@login_required
def timezone_restore(request, timezone_id):
    timezone: TimezoneHandbook = get_object_or_404(TimezoneHandbook, pk=timezone_id)
    timezone.restore(request.user)
    messages.success(request, _('Timezone successfully restored!'))
    return redirect(reverse('handbooks:timezones-list', host='admin'))
