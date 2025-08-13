from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden, HttpResponseRedirect
from django.utils.http import url_has_allowed_host_and_scheme
from django.utils.translation import gettext_lazy as _
from django.shortcuts import render, redirect
from django_hosts import reverse

from .forms import LoginForm


def login_view(request):
    user: User = request.user
    next_page = request.GET.get('next')

    if user.is_authenticated:
        if user.is_active and (user.is_staff or user.is_superuser):
            return HttpResponseForbidden(_('User is not a staff member.'))
        return redirect(next_page or reverse('home', host='admin'))

    initial = {'email': request.COOKIES.get('email', '')}
    form = LoginForm(request.POST or None, initial=initial)
    if form.is_valid():
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password')
        user: User = authenticate(email=email, password=password)

        if not user:
            form.add_error(None, _('User with given credentials not found.'))
        elif not user.is_active:
            form.add_error(None, _('User is not active.'))
        elif not (user.is_staff or user.is_superuser):
            form.add_error(None, _('User is not a staff member.'))
        else:
            login(request, user)
            if next_page and url_has_allowed_host_and_scheme(next_page, allowed_hosts=settings.ALLOWED_HOSTS):
                redirect_url = next_page
            else:
                redirect_url = reverse('home', host='admin')
            response = HttpResponseRedirect(redirect_url)
            response.set_cookie('email', user.email)
            return response

    return render(request, 'Admin/Login/login.html', {'form': form})


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('login', host='admin'))
