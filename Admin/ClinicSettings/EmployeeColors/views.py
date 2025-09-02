from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django_hosts import reverse

from Admin.utils.tables.handler import TableHandler
from core.Colors.models import EmployeeColors
from core.Colors.services import import_colors_from_fixture
from core.Utils.models.exporters import QuerysetExporter
from .tables import EmployeeColorsTable
from .forms import EmployeeColorsForm, EmployeeColorsImportForm
from .filters import EmployeeColorsFilter


@login_required
def color_list(request):
    handler = TableHandler(
        session_key='color_table',
        request=request,
        queryset=EmployeeColors.objects.all(),
        table_class=EmployeeColorsTable,
        filterset_class=EmployeeColorsFilter,
        search_fields=('^name',)
    )
    handler = handler.process()
    table = {
        'handler': handler,
        'title': _('Employee colors list'),
    }
    return render(request, 'Admin/ClinicSettings/EmployeeColors/list.html', {'table': table})


@login_required
def color_add(request):
    if request.POST.get('cancel'):
        return redirect(reverse('clinic-settings:employee-color-list', host='admin'))

    form_body = EmployeeColorsForm(request.POST or None, request.FILES or None, request=request)
    if form_body.is_valid():
        color = form_body.save()
        print('color.created_by', color.created_by)
        print('color.updated_by', color.updated_by)
        return redirect(reverse('clinic-settings:employee-color-view', args=[color.id], host='admin'))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/ClinicSettings/EmployeeColors/add.html', {'form': form})


@login_required
def color_view(request, color_id):
    color: EmployeeColors = get_object_or_404(EmployeeColors, pk=color_id)
    return render(request, 'Admin/ClinicSettings/EmployeeColors/view.html', {'color': color})


@login_required
def color_edit(request, color_id):
    color: EmployeeColors = get_object_or_404(EmployeeColors, pk=color_id)
    if request.POST.get('cancel'):
        return redirect(reverse('clinic-settings:employee-color-view', args=[color.id], host='admin'))

    form_body = EmployeeColorsForm(request.POST or None, request.FILES or None, request=request,
                                   instance=color)
    if form_body.is_valid():
        color = form_body.save()
        print('color.created_by', color.created_by)
        print('color.updated_by', color.updated_by)
        return redirect(reverse('clinic-settings:employee-color-view', args=[color.id], host='admin'))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/ClinicSettings/EmployeeColors/edit.html', {'color': color, 'form': form})


@login_required
def color_archive(request, color_id):
    color: EmployeeColors = get_object_or_404(EmployeeColors, pk=color_id)
    color.archive(request.user)
    return JsonResponse({'success': True, 'is_active': color.is_active})


@login_required
def color_restore(request, color_id):
    color: EmployeeColors = get_object_or_404(EmployeeColors, pk=color_id)
    color.restore(request.user)
    return JsonResponse({'success': True, 'is_active': color.is_active})


@login_required
def color_set_default(request, color_id):
    color: EmployeeColors = get_object_or_404(EmployeeColors, pk=color_id)
    color = EmployeeColors.set_default(color)
    return JsonResponse({'success': True, 'is_default': color.is_default})


@login_required
def color_import(request):
    if request.POST.get('cancel'):
        return redirect(reverse('clinic-settings:employee-color-list', host='admin'))

    form_body = EmployeeColorsImportForm(request.POST or None, request.FILES or None)
    if form_body.is_valid():
        try:
            form_body.save()
            messages.success(request, _('Employee colors load successfully!'))
            return redirect(reverse('clinic-settings:employee-color-list', host='admin'))
        except Exception as e:
            messages.error(request, _('Unable to load file: %s') % str(e))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/ClinicSettings/EmployeeColors/import.html', {'form': form})


@login_required
def color_export(request, mode: str):
    exporter = QuerysetExporter(mode=mode,
                                queryset=EmployeeColors.objects.active().order_by('name'),
                                fields=('name', 'sideline', 'background', 'is_default'))
    content = exporter.get_content()
    response = HttpResponse(content, content_type=exporter.get_content_type())
    filename = f'{settings.APP_NAME} color {timezone.now()}.{exporter.get_extension()}'
    response["Content-Disposition"] = f'attachment; filename="{filename}"'
    return response


@login_required
def color_sync(request):
    try:
        import_colors_from_fixture()
        messages.success(request, _('Employee colors successfully synchronized with fixture!'))
    except Exception as e:
        messages.error(request, _('Employee colors not synchronized with fixture! Exception raised: %s') % e)
    return redirect(reverse('clinic-settings:employee-color-list', host='admin'))
