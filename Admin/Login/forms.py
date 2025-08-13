from django import forms
from django.utils.translation import gettext_lazy as _


class LoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': _('Enter your email')}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': _('Enter your password')}))
