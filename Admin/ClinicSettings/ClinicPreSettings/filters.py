import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _
from Admin.utils.filters.fields import IsActiveMixinField
from core.ClinicPreSettings.models import ClinicPreSettings
from core.Country.models import Country


class ClinicPreSettingsFilter(django_filters.FilterSet):
    is_active = IsActiveMixinField(required=False)
    country = django_filters.ModelChoiceFilter(label=_('Country'), widget=forms.Select(attrs={'class': 'select2'}),
                                               queryset=Country.objects.active())

    class Meta:
        model = ClinicPreSettings
        fields = ('is_active', 'country')
