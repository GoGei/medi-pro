from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_hosts import reverse

from Admin.utils.tables.handler import TableHandler
from core.Country.models import Country
from core.Country.services import import_countries_from_fixture, import_countries_from_external_api
from core.Utils.models.exporters import QuerysetExporter
from .tables import CountryTable
from .forms import CountryEditForm, CountryImportForm
from .filters import CountryFilter


@login_required
def country_list(request):
    handler = TableHandler(
        session_key='country_table',
        request=request,
        queryset=Country.objects.all(),
        table_class=CountryTable,
        filterset_class=CountryFilter,
        search_fields=('^name', '^cca2', '^ccn3')
    )
    handler = handler.process()
    table = {
        'handler': handler,
        'title': _('Country handbooks list'),
    }
    return render(request, 'Admin/Handbooks/Country/list.html', {'table': table})


@login_required
def country_view(request, country_id):
    country: Country = get_object_or_404(Country, pk=country_id)
    return render(request, 'Admin/Handbooks/Country/view.html', {'country': country})


@login_required
def country_edit(request, country_id):
    country: Country = get_object_or_404(Country, pk=country_id)
    if request.POST.get('cancel'):
        return redirect(reverse('handbooks:country-view', args=[country.id], host='admin'))

    form_body = CountryEditForm(request.POST or None, request.FILES or None, request=request,
                                instance=country)
    if form_body.is_valid():
        country = form_body.save()
        return redirect(reverse('handbooks:country-view', args=[country.id], host='admin'))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/Handbooks/Country/edit.html', {'country': country, 'form': form})


@login_required
def country_archive(request, country_id):
    country: Country = get_object_or_404(Country, pk=country_id)
    country.archive(request.user)
    messages.success(request, _('Country successfully archived!'))
    return redirect(reverse('handbooks:country-list', host='admin'))


@login_required
def country_restore(request, country_id):
    country: Country = get_object_or_404(Country, pk=country_id)
    country.restore(request.user)
    messages.success(request, _('Country successfully restored!'))
    return redirect(reverse('handbooks:country-list', host='admin'))


@login_required
def country_import(request):
    if request.POST.get('cancel'):
        return redirect(reverse('handbooks:country-list', host='admin'))

    form_body = CountryImportForm(request.POST or None, request.FILES or None)
    if form_body.is_valid():
        try:
            form_body.save()
            messages.success(request, _('Country load successfully!'))
            return redirect(reverse('handbooks:country-list', host='admin'))
        except Exception as e:
            messages.error(request, _('Unable to load file: %s') % str(e))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/Handbooks/Country/import.html', {'form': form})


@login_required
def country_export(request, mode: str):
    exporter = QuerysetExporter(mode=mode,
                                queryset=Country.objects.all().order_by('name'),
                                fields=('name', 'cca2', 'ccn3'))
    content = exporter.get_content()
    response = HttpResponse(content, content_type=exporter.get_content_type())
    filename = f'{settings.APP_NAME} country {timezone.now()}.{exporter.get_extension()}'
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response


@login_required
def country_sync(request):
    try:
        import_countries_from_fixture()
        messages.success(request, _('Country successfully synchronized with fixture!'))
    except Exception as e:
        messages.error(request, _('Country not synchronized with fixture! Exception raised: %s') % e)
    return redirect(reverse('handbooks:country-list', host='admin'))


@login_required
def country_sync_external_api(request):
    try:
        import_countries_from_external_api()
        messages.success(request, _('Country successfully synchronized with external API!'))
    except Exception as e:
        messages.error(request, _('Country not synchronized with external API! Exception raised: %s') % e)
    return redirect(reverse('handbooks:country-list', host='admin'))
