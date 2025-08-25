from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone as dj_timezone
from django.utils.translation import gettext_lazy as _
from django_hosts import reverse

from Admin.utils.tables.handler import TableHandler
from core.Timezones.models import TimezoneHandbook
from core.Timezones.services import import_timezones
from core.Utils.models.exporters import QuerysetExporter
from .tables import TimezoneHandbookTable
from .forms import TimezoneHandbookEditForm, TimezoneHandbookImportForm
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


@login_required
def timezone_import(request):
    if request.POST.get('cancel'):
        return redirect(reverse('handbooks:timezones-list', host='admin'))

    form_body = TimezoneHandbookImportForm(request.POST or None, request.FILES or None)
    if form_body.is_valid():
        try:
            form_body.save()
            messages.success(request, _('Timezones load successfully!'))
            return redirect(reverse('handbooks:timezones-list', host='admin'))
        except Exception as e:
            messages.error(request, _('Unable to load file: %s') % str(e))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/Handbooks/TimezoneHandbooks/import.html', {'form': form})


@login_required
def timezone_export(request, mode: str):
    exporter = QuerysetExporter(mode=mode,
                                queryset=TimezoneHandbook.objects.all().order_by('name'),
                                fields=('name', 'offset', 'label'))
    content = exporter.get_content()
    response = HttpResponse(content, content_type=exporter.get_content_type())
    filename = f'{settings.APP_NAME} timezones {dj_timezone.now()}.{exporter.get_extension()}'
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response


@login_required
def timezone_sync(request):
    import_timezones()
    messages.success(request, _('Timezone successfully synchronized!'))
    return redirect(reverse('handbooks:timezones-list', host='admin'))
