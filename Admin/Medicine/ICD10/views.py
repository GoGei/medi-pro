from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_hosts import reverse

from Admin.utils.tables.handler import TableHandler
from core.Medicine.models import ICD10
from core.Medicine.tasks import load_icd10
from core.Utils.models.exporters import QuerysetExporter
from .tables import ICD10Table
from .filters import ICD10Filter


@login_required
def icd10_list(request):
    handler = TableHandler(
        session_key='icd10_table',
        request=request,
        queryset=ICD10.objects.all(),
        table_class=ICD10Table,
        filterset_class=ICD10Filter,
        search_fields=('^name', '^code')
    )
    handler = handler.process()
    table = {
        'handler': handler,
        'title': _('ICD-10 handbooks list'),
    }
    return render(request, 'Admin/Medicine/ICD10/list.html', {'table': table})


@login_required
def icd10_view(request, icd10_id):
    icd10: ICD10 = get_object_or_404(ICD10, pk=icd10_id)
    return render(request, 'Admin/Medicine/ICD10/view.html', {'icd10': icd10})


@login_required
def icd10_export(request, mode: str):
    exporter = QuerysetExporter(mode=mode,
                                queryset=ICD10.objects.all().order_by('name'),
                                fields=('name', 'code', 'source'))
    content = exporter.get_content()
    response = HttpResponse(content, content_type=exporter.get_content_type())
    filename = f'{settings.APP_NAME} allergy type {timezone.now()}.{exporter.get_extension()}'
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response


@login_required
def icd10_sync(request):
    try:
        load_icd10.apply_async()
        messages.success(request, _('Command to load allergy causes launched!'))
    except Exception as e:
        messages.error(request, _('Command to load allergy causes failed! Exception raised: %s') % e)
    return redirect(reverse('medicine:icd10-list', host='admin'))
