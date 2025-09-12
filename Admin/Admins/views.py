from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext_lazy as _
from django_hosts import reverse

from Admin.utils.forms.fields import PasswordField
from Admin.utils.tables.handler import TableHandler
from core.User.models import User
from .tables import AdminsTable
from .forms import AdminsForm, AdminsSetPasswordForm
from .filters import AdminsFilter


def _get_queryset():
    return User.objects.admins()


@login_required
def admins_list(request):
    handler = TableHandler(
        session_key='admins_table',
        request=request,
        queryset=_get_queryset(),
        table_class=AdminsTable,
        filterset_class=AdminsFilter,
        search_fields=('^email',)
    )
    handler = handler.process()
    table = {
        'handler': handler,
        'title': _('Admins list'),
    }
    return render(request, 'Admin/Admins/list.html', {'table': table})


@login_required
def admins_add(request):
    if request.POST.get('cancel'):
        return redirect(reverse('admins-list', host='admin'))

    form_body = AdminsForm(request.POST or None, request.FILES or None, request=request)
    if form_body.is_valid():
        user: User = form_body.save()
        messages.success(request, _('Admins created successfully!'))
        if request.user.is_superuser:
            return redirect(reverse('admins-set-password', args=[user.id], host='admin'))
        return redirect(reverse('admins-view', args=[user.id], host='admin'))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/Admins/add.html', {'form': form})


@login_required
def admins_view(request, admins_id):
    user: User = get_object_or_404(_get_queryset(), pk=admins_id)
    return render(request, 'Admin/Admins/view.html', {'user': user})


@login_required
def admins_edit(request, admins_id):
    user: User = get_object_or_404(_get_queryset(), pk=admins_id)
    if request.POST.get('cancel'):
        return redirect(reverse('admins-view', args=[user.id], host='admin'))

    form_body = AdminsForm(request.POST or None, request.FILES or None, request=request,
                           instance=user)
    if form_body.is_valid():
        user: User = form_body.save()
        messages.success(request, _('Admin edited successfully!'))
        return redirect(reverse('admins-view', args=[user.id], host='admin'))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/Admins/edit.html', {'user': user, 'form': form})


@login_required
def admins_archive(request, admins_id):
    user: User = get_object_or_404(_get_queryset(), pk=admins_id)
    user.is_active = False
    user.save(update_fields=['is_active'])
    return JsonResponse({'success': True, 'is_active': user.is_active})


@login_required
def admins_restore(request, admins_id):
    user: User = get_object_or_404(_get_queryset(), pk=admins_id)
    user.is_active = True
    user.save(update_fields=['is_active'])
    return JsonResponse({'success': True, 'is_active': user.is_active})


@login_required
def admins_set_password(request, admins_id):
    user: User = get_object_or_404(_get_queryset(), pk=admins_id)
    if request.POST.get('cancel'):
        return redirect(reverse('admins-view', args=[user.id], host='admin'))

    form_body = AdminsSetPasswordForm(request.POST or None, request.FILES or None, request=request,
                                      instance=user)
    if form_body.is_valid():
        user: User = form_body.save()
        messages.success(request, _('Admin reset password successfully!'))
        if user.id == request.user.id:
            update_session_auth_hash(request, user)
        return redirect(reverse('admins-view', args=[user.id], host='admin'))

    form = {
        'form_body': form_body,
        'informer': PasswordField.DEFAULT_INFORMER,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/Admins/set_password.html', {'user': user, 'form': form})
