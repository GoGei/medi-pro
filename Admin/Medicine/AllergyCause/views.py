from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_hosts import reverse

from Admin.utils.tables.handler import TableHandler
from core.Medicine.models import AllergyCause
from core.Medicine.tasks import extract_allergy_cause
from core.Utils.models.exporters import QuerysetExporter
from .tables import AllergyCauseTable
from .filters import AllergyCauseFilter


@login_required
def allergy_cause_list(request):
    handler = TableHandler(
        session_key='allergy_cause_table',
        request=request,
        queryset=AllergyCause.objects.all(),
        table_class=AllergyCauseTable,
        filterset_class=AllergyCauseFilter,
        search_fields=('^name', '^code')
    )
    handler = handler.process()
    table = {
        'handler': handler,
        'title': _('Allergy type handbooks list'),
    }
    return render(request, 'Admin/Medicine/AllergyCause/list.html', {'table': table})


@login_required
def allergy_cause_view(request, allergy_cause_id):
    allergy_cause: AllergyCause = get_object_or_404(AllergyCause, pk=allergy_cause_id)
    return render(request, 'Admin/Medicine/AllergyCause/view.html', {'allergy_cause': allergy_cause})


@login_required
def allergy_cause_export(request, mode: str):
    exporter = QuerysetExporter(mode=mode,
                                queryset=AllergyCause.objects.all().order_by('name'),
                                fields=('name', 'code', 'source', 'is_active'))
    content = exporter.get_content()
    response = HttpResponse(content, content_type=exporter.get_content_type())
    filename = f'{settings.APP_NAME} allergy type {timezone.now()}.{exporter.get_extension()}'
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response


@login_required
def allergy_cause_sync(request):
    try:
        extract_allergy_cause.apply_async()
        messages.success(request, _('Command to load allergy causes launched!'))
    except Exception as e:
        messages.error(request, _('Command to load allergy causes failed! Exception raised: %s') % e)
    return redirect(reverse('medicine:allergy-causes-list', host='admin'))
