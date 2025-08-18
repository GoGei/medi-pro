import json
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from Admin.utils.forms.base import BaseModelForm
from core.Timezones.models import TimezoneHandbook


class TimezoneHandbookEditForm(BaseModelForm):
    offset = forms.CharField(label=_('Offset'), max_length=TimezoneHandbook.name.field.max_length)
    label = forms.CharField(label=_('Label'), max_length=TimezoneHandbook.label.field.max_length)

    class Meta:
        model = TimezoneHandbook
        fields = ('offset', 'label')


class TimezoneHandbookImportForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'accept': 'application/json'})
    )

    def clean_file(self):
        uploaded_file = self.cleaned_data['file']
        if uploaded_file.content_type not in ('application/json', 'text/json'):
            self.add_error(None, 'File must be a valid JSON file')

        try:
            content = uploaded_file.read().decode('utf-8')
            json.loads(content)
            uploaded_file.seek(0)
        except Exception:
            self.add_error(None, _('Uploaded file is not a valid JSON'))

        return uploaded_file

    def save(self):
        pass
