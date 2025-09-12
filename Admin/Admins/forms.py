from django.utils.translation import gettext_lazy as _
from Admin.utils.forms.base import BaseModelForm
from Admin.utils.forms.fields import PasswordField
from core.User.models import User


class AdminsForm(BaseModelForm):
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'is_superuser', 'is_active')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.request
        user: User = request.user

        if not user.is_superuser:
            self.fields['is_superuser'].disabled = True
            if self.instance and self.instance.is_superuser:
                self.fields['is_active'].disabled = True

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            return email

        email = email.lower().strip()
        qs = User.objects.filter(email__iexact=email)
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            self.add_error('email', _('User with this email already exists'))
        return email

    def save(self, commit=True):
        instance = super().save(commit=False)
        instance.is_staff = True
        if commit:
            instance.save()
        return instance


class AdminsSetPasswordForm(BaseModelForm):
    password = PasswordField()
    confirm = PasswordField()

    class Meta:
        model = User
        fields = ('password', 'confirm')

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
        return data

    def save(self, commit=True):
        user: User = self.instance
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user
