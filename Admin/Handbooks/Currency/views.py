from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_hosts import reverse

from Admin.utils.tables.handler import TableHandler
from core.ClinicPreSettings.models import ClinicPreSettings
from core.Currency.models import Currency
from core.Currency.services import import_currencies_from_fixture
from core.Utils.models.exporters import QuerysetExporter
from .tables import CurrencyTable
from .forms import CurrencyForm, CurrencyImportForm
from .filters import CurrencyFilter


@login_required
def currency_list(request):
    handler = TableHandler(
        session_key='currency_table',
        request=request,
        queryset=Currency.objects.all(),
        table_class=CurrencyTable,
        filterset_class=CurrencyFilter,
        search_fields=('name', '^code')
    )
    handler = handler.process()
    table = {
        'handler': handler,
        'title': _('Currency handbooks list'),
    }
    return render(request, 'Admin/Handbooks/Currency/list.html', {'table': table})


@login_required
def currency_add(request):
    if request.POST.get('cancel'):
        return redirect(reverse('handbooks:currency-list', host='admin'))

    form_body = CurrencyForm(request.POST or None, request.FILES or None, request=request)
    if form_body.is_valid():
        currency = form_body.save()
        return redirect(reverse('handbooks:currency-view', args=[currency.id], host='admin'))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/Handbooks/Currency/add.html', {'form': form})


@login_required
def currency_view(request, currency_id):
    currency: Currency = get_object_or_404(Currency, pk=currency_id)
    return render(request, 'Admin/Handbooks/Currency/view.html', {'currency': currency})


@login_required
def currency_edit(request, currency_id):
    currency: Currency = get_object_or_404(Currency, pk=currency_id)
    if request.POST.get('cancel'):
        return redirect(reverse('handbooks:currency-view', args=[currency.id], host='admin'))

    form_body = CurrencyForm(request.POST or None, request.FILES or None, request=request,
                             instance=currency)
    if form_body.is_valid():
        currency = form_body.save()
        return redirect(reverse('handbooks:currency-view', args=[currency.id], host='admin'))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/Handbooks/Currency/edit.html', {'currency': currency, 'form': form})


@login_required
def currency_archive(request, currency_id):
    currency: Currency = get_object_or_404(Currency, pk=currency_id)
    related_settings = ClinicPreSettings.objects.active().filter(currencies=currency)
    if related_settings.exists():
        msg = _('For given currency there are still active related settings')
        return JsonResponse({'success': False, 'is_active': currency.is_active, 'msg': msg,
                             'related_settings': list(related_settings.values_list('id', flat=True))}, status=400)

    currency.archive(request.user)
    return JsonResponse({'success': True, 'is_active': currency.is_active})


@login_required
def currency_restore(request, currency_id):
    currency: Currency = get_object_or_404(Currency, pk=currency_id)
    currency.restore(request.user)
    return JsonResponse({'success': True, 'is_active': currency.is_active})


@login_required
def currency_import(request):
    if request.POST.get('cancel'):
        return redirect(reverse('handbooks:currency-list', host='admin'))

    form_body = CurrencyImportForm(request.POST or None, request.FILES or None)
    if form_body.is_valid():
        try:
            form_body.save()
            messages.success(request, _('Currency load successfully!'))
            return redirect(reverse('handbooks:currency-list', host='admin'))
        except Exception as e:
            messages.error(request, _('Unable to load file: %s') % str(e))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/Handbooks/Currency/import.html', {'form': form})


@login_required
def currency_export(request, mode: str):
    exporter = QuerysetExporter(mode=mode,
                                queryset=Currency.objects.active().order_by('id'),
                                fields=('name', 'code', 'symbol'))
    content = exporter.get_content()
    response = HttpResponse(content, content_type=exporter.get_content_type())
    filename = f'{settings.APP_NAME} currency {timezone.now()}.{exporter.get_extension()}'
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response


@login_required
def currency_sync(request):
    try:
        import_currencies_from_fixture()
        messages.success(request, _('Currency successfully synchronized with fixture!'))
    except Exception as e:
        messages.error(request, _('Currency not synchronized with fixture! Exception raised: %s') % e)
    return redirect(reverse('handbooks:currency-list', host='admin'))
