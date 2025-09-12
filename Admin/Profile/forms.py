from django import forms
from django.utils.translation import gettext_lazy as _
from Admin.utils.forms.base import BaseModelForm
from Admin.utils.forms.fields import PasswordField
from core.User.models import User


class ProfileSetPasswordForm(BaseModelForm):
    old_password = forms.CharField(min_length=1, widget=forms.PasswordInput)
    password = PasswordField()
    confirm = PasswordField()

    class Meta:
        model = User
        fields = ('old_password', 'password', 'confirm')

    def clean(self):
        data = super().clean()
        password: str = data.get('password')
        confirm: str = data.get('confirm')

        if (password and confirm) and (password != confirm):
            msg = _('Password mismatch')
            self.add_error('password', msg)
            self.add_error('confirm', msg)

        if not self.instance:
            self.add_error(None, _('Instance is missing! Please, contact administrator'))

        old_password: str = data.get('old_password')
        if self.instance and old_password and not self.instance.check_password(old_password):
            self.add_error(None, _('Password entered incorrectly'))
        return data

    def save(self, commit=True):
        user: User = self.instance
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class ProfileEditForm(BaseModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')
