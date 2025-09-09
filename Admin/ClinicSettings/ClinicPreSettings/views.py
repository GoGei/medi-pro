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
from core.Loggers.models import HandbookUpdateLog
from core.Utils.models.exporters import ExportModes, QuerysetExporter
from .tables import ClinicPreSettingsTable
from .forms import ClinicPreSettingsForm, ClinicPreSettingsImportForm
from .filters import ClinicPreSettingsFilter


@login_required
def setting_list(request):
    handler = TableHandler(
        session_key='setting_table',
        request=request,
        queryset=(
            ClinicPreSettings.objects
            .select_related('country', 'primary_timezone', 'primary_currency')
            .prefetch_related('timezones', 'currencies')
            .all()
        ),
        table_class=ClinicPreSettingsTable,
        filterset_class=ClinicPreSettingsFilter,
        search_fields=('^country__name', 'country__cca2', 'country__ccn3')
    )
    handler = handler.process()
    table = {
        'handler': handler,
        'title': _('Clinic pre-settings list'),
    }
    return render(request, 'Admin/ClinicSettings/ClinicPreSettings/list.html', {'table': table})


@login_required
def setting_add(request):
    if request.POST.get('cancel'):
        return redirect(reverse('clinic-settings:clinic-pre-settings-list', host='admin'))

    form_body = ClinicPreSettingsForm(request.POST or None, request.FILES or None, request=request)
    if form_body.is_valid():
        setting = form_body.save()
        messages.success(request, _('Setting created successfully!'))
        return redirect(reverse('clinic-settings:clinic-pre-settings-view', args=[setting.id], host='admin'))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/ClinicSettings/ClinicPreSettings/add.html', {'form': form})


@login_required
def setting_view(request, setting_id):
    qs = (
        ClinicPreSettings.objects
        .select_related('country', 'primary_timezone', 'primary_currency')
        .prefetch_related('timezones', 'currencies')
    )
    setting: ClinicPreSettings = get_object_or_404(qs, pk=setting_id)
    return render(request, 'Admin/ClinicSettings/ClinicPreSettings/view.html', {'setting': setting})


@login_required
def setting_edit(request, setting_id):
    setting: ClinicPreSettings = get_object_or_404(ClinicPreSettings, pk=setting_id)
    if request.POST.get('cancel'):
        return redirect(reverse('clinic-settings:clinic-pre-settings-view', args=[setting.id], host='admin'))

    form_body = ClinicPreSettingsForm(request.POST or None, request.FILES or None, request=request,
                                      instance=setting)
    if form_body.is_valid():
        setting = form_body.save()
        messages.success(request, _('Setting edited successfully!'))
        return redirect(reverse('clinic-settings:clinic-pre-settings-view', args=[setting.id], host='admin'))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/ClinicSettings/ClinicPreSettings/edit.html', {'setting': setting, 'form': form})


@login_required
def setting_archive(request, setting_id):
    setting: ClinicPreSettings = get_object_or_404(ClinicPreSettings, pk=setting_id)
    setting.archive(request.user)
    return JsonResponse({'success': True, 'is_active': setting.is_active})


@login_required
def setting_restore(request, setting_id):
    setting: ClinicPreSettings = get_object_or_404(ClinicPreSettings, pk=setting_id)
    if ClinicPreSettings.get_setting(country=setting.country):
        msg = _('For given country default setting already presented!')
        return JsonResponse({'success': False, 'is_active': setting.is_active, 'msg': msg}, status=400)
    setting.restore(request.user)
    return JsonResponse({'success': True, 'is_active': setting.is_active})


@login_required
def setting_import(request):
    if request.POST.get('cancel'):
        return redirect(reverse('clinic-settings:clinic-pre-settings-list', host='admin'))

    form_body = ClinicPreSettingsImportForm(request.POST or None, request.FILES or None)
    if form_body.is_valid():
        try:
            form_body.save()
            HandbookUpdateLog.objects.create(user_id=request.user.id,
                                             handbook=HandbookUpdateLog.HandbookChoices.CLINIC_PRE_SETTINGS)
            messages.success(request, _('Settings imported successfully!'))
            return redirect(reverse('clinic-settings:clinic-pre-settings-list', host='admin'))
        except Exception as e:
            messages.error(request, _('Unable to load file: %s') % str(e))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/ClinicSettings/ClinicPreSettings/import.html', {'form': form})


def __setting_export(func, mode):
    qs = (
        ClinicPreSettings.objects
        .select_related('country', 'primary_timezone', 'primary_currency')
        .prefetch_related('timezones', 'currencies')
        .active().order_by('country__ccn3')
    )
    exporter = QuerysetExporter(mode=mode,
                                queryset=qs,
                                obj_to_dict_func=func,
                                fields=(
                                    'country_name',
                                    'country_ccn3',
                                    'timezone_name',
                                    'currency_name',
                                    'currency_code',
                                    'timezone_names',
                                    'currency_codes',
                                    'currency_names'
                                ))
    content = exporter.get_content()
    response = HttpResponse(content, content_type=exporter.get_content_type())
    filename = f'{settings.APP_NAME} clinic pre-settings {timezone.now()}.{exporter.get_extension()}'
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response


@login_required
def setting_export_csv(request):
    obj_to_dict_func = lambda item: {  # noqa E731
        'country_name': item.country.name,
        'country_ccn3': item.country.ccn3,
        'timezone_name': item.primary_timezone.name,
        'currency_name': item.primary_currency.name,
        'currency_code': item.primary_currency.code,
        'timezone_names': ','.join([x.name for x in item.timezones.all()]),
        'currency_codes': ','.join([x.code for x in item.currencies.all()]),
        'currency_names': ','.join([x.name for x in item.currencies.all()]),
    }
    return __setting_export(obj_to_dict_func, mode=ExportModes.CSV)


@login_required
def setting_export_json(request):
    obj_to_dict_func = lambda item: {  # noqa E731
        'country_name': item.country.name,
        'country_ccn3': item.country.ccn3,
        'timezone_name': item.primary_timezone.name,
        'currency_name': item.primary_currency.name,
        'currency_code': item.primary_currency.code,
        'timezone_names': [x.name for x in item.timezones.all()],
        'currency_codes': [x.code for x in item.currencies.all()],
        'currency_names': [x.name for x in item.currencies.all()],
    }
    return __setting_export(obj_to_dict_func, mode=ExportModes.JSON)
