from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.translation import gettext_lazy as _
from django_hosts import reverse

from Admin.utils.forms.fields import PasswordField
from core.User.models import User
from .forms import ProfileSetPasswordForm, ProfileEditForm


@login_required
def profile_view(request):
    return render(request, 'Admin/Profile/view.html', {'user': request.user})


@login_required
def profile_change_password(request):
    if request.POST.get('cancel'):
        return redirect(reverse('profile-view', args=[request.user.id], host='admin'))

    form_body = ProfileSetPasswordForm(request.POST or None, request.FILES or None, request=request,
                                       instance=request.user)
    if form_body.is_valid():
        user: User = form_body.save()
        messages.success(request, _('Change password successfully!'))
        update_session_auth_hash(request, user)
        return redirect(reverse('profile-view', host='admin'))

    form = {
        'form_body': form_body,
        'informer': PasswordField.DEFAULT_INFORMER,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/Profile/change_password.html', {'user': request.user, 'form': form})


@login_required
def profile_edit(request):
    if request.POST.get('cancel'):
        return redirect(reverse('profile-view', host='admin'))

    form_body = ProfileEditForm(request.POST or None, request.FILES or None, request=request,
                                instance=request.user)
    if form_body.is_valid():
        form_body.save()
        messages.success(request, _('Change profile successfully!'))
        return redirect(reverse('profile-view', host='admin'))

    form = {
        'form_body': form_body,
        'buttons': {
            'submit': True,
            'cancel': True,
        }
    }
    return render(request, 'Admin/Profile/edit.html', {'user': request.user, 'form': form})
