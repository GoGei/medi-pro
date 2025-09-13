from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from Admin.utils.tables.handler import TableHandler
from core.Medicine.models import AllergyReaction
from core.Utils.models.exporters import QuerysetExporter
from .tables import AllergyReactionTable
from .filters import AllergyReactionFilter


@login_required
def allergy_reaction_list(request):
    handler = TableHandler(
        session_key='allergy_reaction_table',
        request=request,
        queryset=AllergyReaction.objects.all(),
        table_class=AllergyReactionTable,
        filterset_class=AllergyReactionFilter,
        search_fields=('^name', '^code')
    )
    handler = handler.process()
    table = {
        'handler': handler,
        'title': _('Allergy reaction handbooks list'),
    }
    return render(request, 'Admin/Medicine/AllergyReaction/list.html', {'table': table})


@login_required
def allergy_reaction_view(request, allergy_reaction_id):
    allergy_reaction: AllergyReaction = get_object_or_404(AllergyReaction, pk=allergy_reaction_id)
    return render(request, 'Admin/Medicine/AllergyReaction/view.html', {'allergy_reaction': allergy_reaction})


@login_required
def allergy_reaction_export(request, mode: str):
    exporter = QuerysetExporter(mode=mode,
                                queryset=AllergyReaction.objects.all().order_by('name'),
                                fields=('name', 'code', 'source', 'is_active'))
    content = exporter.get_content()
    response = HttpResponse(content, content_reaction=exporter.get_content_type())
    filename = f'{settings.APP_NAME} allergy reaction {timezone.now()}.{exporter.get_extension()}'
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response
