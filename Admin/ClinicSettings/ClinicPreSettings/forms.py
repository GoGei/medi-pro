import json
from django import forms
from django.utils.translation import gettext_lazy as _
from Admin.utils.forms.base import BaseModelForm
from core.ClinicPreSettings.models import ClinicPreSettings
from core.ClinicPreSettings.services import import_clinic_pre_settings
from core.Country.models import Country
from core.Currency.models import Currency
from core.Timezones.models import TimezoneHandbook


class ClinicPreSettingsForm(BaseModelForm):
    country = forms.ModelChoiceField(label=_('Country'), widget=forms.Select(attrs={'class': 'select2'}),
                                     queryset=Country.objects.active())
    timezones = forms.ModelMultipleChoiceField(label=_('Timezones'),
                                               widget=forms.SelectMultiple(attrs={'class': 'select2'}),
                                               queryset=TimezoneHandbook.objects.active())
    primary_timezone = forms.ModelChoiceField(label=_('Primary timezone'),
                                              widget=forms.Select(attrs={'class': 'select2'}),
                                              queryset=TimezoneHandbook.objects.active())
    currencies = forms.ModelMultipleChoiceField(label=_('Currencies'),
                                                widget=forms.SelectMultiple(attrs={'class': 'select2'}),
                                                queryset=Currency.objects.active())
    primary_currency = forms.ModelChoiceField(label=_('Primary currency'),
                                              widget=forms.Select(attrs={'class': 'select2'}),
                                              queryset=Currency.objects.active())

    class Meta:
        model = ClinicPreSettings
        fields = ('country', 'timezones', 'primary_timezone', 'currencies', 'primary_currency')

    def clean_country(self):
        country: Country = self.cleaned_data.get('country')
        if not country:
            return country

        qs = ClinicPreSettings.objects.active().filter(country_id=country.id)
        if self.instance:
            qs = qs.exclude(id=self.instance.id)
        if qs.exists():
            self.add_error('country', _('For given country setting already presented!'))

        return country

    def clean(self):
        data = self.cleaned_data

        timezones: TimezoneHandbook = self.cleaned_data.get('timezones')
        primary_timezone: list[TimezoneHandbook] = self.cleaned_data.get('primary_timezone')
        if timezones and primary_timezone and (primary_timezone not in timezones):
            msg = _('Primary timezone not found in specified timezones')
            self.add_error('primary_timezone', msg)

        currencies: Currency = self.cleaned_data.get('currencies')
        primary_currency: list[Currency] = self.cleaned_data.get('primary_currency')
        if currencies and primary_currency and (primary_currency not in currencies):
            msg = _('Primary timezone not found in specified currencies')
            self.add_error('primary_currency', msg)

        return data


class ClinicPreSettingsImportForm(forms.Form):
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
        return import_clinic_pre_settings(self.json_data)
