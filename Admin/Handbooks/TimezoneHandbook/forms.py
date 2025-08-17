from django import forms
from django.utils.translation import gettext_lazy as _
from Admin.utils.forms.base import BaseModelForm
from core.Timezones.models import TimezoneHandbook


class TimezoneHandbookEditForm(BaseModelForm):
    offset = forms.CharField(label=_('Offset'), max_length=TimezoneHandbook.name.field.max_length)
    label = forms.CharField(label=_('Label'), max_length=TimezoneHandbook.label.field.max_length)

    class Meta:
        model = TimezoneHandbook
        fields = ('offset', 'label')
