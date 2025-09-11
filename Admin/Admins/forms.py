from django.utils.translation import gettext_lazy as _
from Admin.utils.forms.base import BaseModelForm
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

    def clean(self):
        super().clean()
        data = self.cleaned_data
        data['is_staff'] = True
        return data
