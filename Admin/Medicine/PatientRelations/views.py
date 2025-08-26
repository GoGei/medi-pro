from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from Admin.utils.tables.handler import TableHandler
from core.Medicine.models import PatientRelation
from core.Utils.models.exporters import QuerysetExporter
from .tables import PatientRelationTable
from .filters import PatientRelationFilter


@login_required
def patient_relation_list(request):
    handler = TableHandler(
        session_key='patient_relation_table',
        request=request,
        queryset=PatientRelation.objects.all(),
        table_class=PatientRelationTable,
        filterset_class=PatientRelationFilter,
        search_fields=('^name',)
    )
    handler = handler.process()
    table = {
        'handler': handler,
        'title': _('Patient relations handbooks list'),
    }
    return render(request, 'Admin/Medicine/PatientRelation/list.html', {'table': table})


@login_required
def patient_relation_view(request, patient_relation_id):
    patient_relation: PatientRelation = get_object_or_404(PatientRelation, pk=patient_relation_id)
    return render(request, 'Admin/Medicine/PatientRelation/view.html', {'patient_relation': patient_relation})


@login_required
def patient_relation_export(request, mode: str):
    exporter = QuerysetExporter(mode=mode,
                                queryset=PatientRelation.objects.all().order_by('name'),
                                fields=('name',))
    content = exporter.get_content()
    response = HttpResponse(content, content_type=exporter.get_content_type())
    filename = f'{settings.APP_NAME} patient relations {timezone.now()}.{exporter.get_extension()}'
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response
