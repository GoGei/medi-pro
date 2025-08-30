from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_hosts import reverse

from Admin.utils.tables.handler import TableHandler
from core.Medicine.models import AllergyType
from core.Medicine.tasks import extract_allergy_types
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
                                fields=('name', 'code', 'source'))
    content = exporter.get_content()
    response = HttpResponse(content, content_type=exporter.get_content_type())
    filename = f'{settings.APP_NAME} allergy type {timezone.now()}.{exporter.get_extension()}'
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response


@login_required
def allergy_type_sync(request):
    try:
        extract_allergy_types.apply_async()
        messages.success(request, _('Command to load allergy causes launched!'))
    except Exception as e:
        messages.error(request, _('Command to load allergy causes failed! Exception raised: %s') % e)
    return redirect(reverse('medicine:allergy-types-list', host='admin'))
