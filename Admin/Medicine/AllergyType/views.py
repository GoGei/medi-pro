from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from Admin.utils.tables.handler import TableHandler
from core.Medicine.models import AllergyType
from core.Utils.models.exporters import QuerysetExporter
from .tables import AllergyTypeTable
from .filters import AllergyTypeFilter


@login_required
def allergy_type_list(request):
    handler = TableHandler(
        session_key='allergy_type_table',
        request=request,
        queryset=AllergyType.objects.all(),
        table_class=AllergyTypeTable,
        filterset_class=AllergyTypeFilter,
        search_fields=('^name', '^code')
    )
    handler = handler.process()
    table = {
        'handler': handler,
        'title': _('Allergy type handbooks list'),
    }
    return render(request, 'Admin/Medicine/AllergyType/list.html', {'table': table})


@login_required
def allergy_type_view(request, allergy_type_id):
    allergy_type: AllergyType = get_object_or_404(AllergyType, pk=allergy_type_id)
    return render(request, 'Admin/Medicine/AllergyType/view.html', {'allergy_type': allergy_type})


@login_required
def allergy_type_export(request, mode: str):
    exporter = QuerysetExporter(mode=mode,
                                queryset=AllergyType.objects.all().order_by('name'),
                                fields=('name', 'code', 'source', 'is_active'))
    content = exporter.get_content()
    response = HttpResponse(content, content_type=exporter.get_content_type())
    filename = f'{settings.APP_NAME} allergy type {timezone.now()}.{exporter.get_extension()}'
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response
