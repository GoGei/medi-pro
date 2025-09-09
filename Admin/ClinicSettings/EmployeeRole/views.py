from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django_hosts import reverse

from Admin.utils.tables.handler import TableHandler
from core.Employee.models import EmployeeRole
from .tables import EmployeeRoleTable
from .forms import EmployeeRoleForm
from .filters import EmployeeRoleFilter


@login_required
def role_list(request):
    handler = TableHandler(
        session_key='employee_role_table',
        request=request,
        queryset=EmployeeRole.objects.all(),
        table_class=EmployeeRoleTable,
        filterset_class=EmployeeRoleFilter,
        search_fields=('^name',)
    )
    handler = handler.process()
    table = {
        'handler': handler,
        'title': _('Employee roles list'),
    }
    return render(request, 'Admin/ClinicSettings/EmployeeRole/list.html', {'table': table})


@login_required
def role_view(request, role_id):
    role: EmployeeRole = get_object_or_404(EmployeeRole, pk=role_id)
    return render(request, 'Admin/ClinicSettings/EmployeeRole/view.html', {'role': role})


@login_required
def role_edit(request, role_id):
    role: EmployeeRole = get_object_or_404(EmployeeRole, pk=role_id)
    if request.POST.get('cancel'):
        return redirect(reverse('clinic-settings:employee-role-view', args=[role.id], host='admin'))

    form_body = EmployeeRoleForm(request.POST or None, request.FILES or None, request=request,
                                 instance=role)
    if form_body.is_valid():
        role = form_body.save()
        messages.success(request, _('Employee role edited successfully!'))
        return redirect(reverse('clinic-settings:employee-role-view', args=[role.id], host='admin'))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/ClinicSettings/EmployeeRole/edit.html', {'role': role, 'form': form})
