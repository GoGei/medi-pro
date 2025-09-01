import json
from django import forms
from django.utils.translation import gettext_lazy as _
from Admin.utils.forms.base import BaseModelForm
from Admin.utils.forms.fields import ColorField
from core.Colors.models import EmployeeColors
from core.Colors.services import import_colors_from_fixture


class EmployeeColorsForm(BaseModelForm):
    name = forms.CharField(label=_('Label'), max_length=EmployeeColors.name.field.max_length)
    sideline = ColorField(label=_('Sideline'))
    background = ColorField(label=_('Background'))

    class Meta:
        model = EmployeeColors
        fields = ('name', 'sideline', 'background')

    def save_on_create(self, commit=True):
        if not EmployeeColors.get_default():
            self.cleaned_data['is_default'] = True
        return super().save_on_create(commit=commit)


class EmployeeColorsImportForm(forms.Form):
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
        return import_colors_from_fixture(self.json_data)
