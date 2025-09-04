import json
from django import forms
from django.utils.translation import gettext_lazy as _
from Admin.utils.forms.base import BaseModelForm
from core.Country.models import Country
from core.Country.services import import_countries_from_fixture


class CountryEditForm(BaseModelForm):
    name = forms.CharField(label=_('Label'), max_length=Country.name.field.max_length)

    class Meta:
        model = Country
        fields = ('name',)


class CountryImportForm(forms.Form):
    file = forms.FileField(
        widget=forms.ClearableFileInput(attrs={'accept': 'application/json'})
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.json_data = None

    def clean_file(self):
        uploaded_file = self.cleaned_data['file']
        if uploaded_file.content_type not in ('application/json', 'text/json'):
            self.add_error(None, 'File must be a valid JSON file')

        try:
            content = uploaded_file.read().decode('utf-8')
            self.json_data = json.loads(content)
            uploaded_file.seek(0)
        except Exception:
            self.add_error(None, _('Uploaded file is not a valid JSON'))

        return uploaded_file

    def save(self):
        return import_countries_from_fixture(data=self.json_data)
