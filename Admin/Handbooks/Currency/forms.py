import json
from django import forms
from django.utils.translation import gettext_lazy as _
from Admin.utils.forms.base import BaseModelForm
from core.Currency.models import Currency
from core.Currency.services import import_currencies_from_fixture


class CurrencyForm(BaseModelForm):
    name = forms.CharField(label=_('Name'), max_length=Currency.name.field.max_length)
    code = forms.CharField(label=_('Code'), max_length=Currency.code.field.max_length)
    symbol = forms.CharField(label=_('Symbol'), max_length=Currency.symbol.field.max_length)

    class Meta:
        model = Currency
        fields = ('name', 'code', 'symbol')

    def clean_code(self):
        code = self.cleaned_data.get('code')
        if not code:
            return code

        code = code.strip().upper()
        qs = Currency.objects.filter(code__iexact=code)
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            self.add_error('code', _('This code already presented'))

        return code


class CurrencyImportForm(forms.Form):
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
        return import_currencies_from_fixture(data=self.json_data)
