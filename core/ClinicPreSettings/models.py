from django.db import models
from django.utils.translation import gettext_lazy as _
from core.Utils.models.mixins import IsActiveMixin


class ClinicPreSettings(IsActiveMixin):
    country = models.ForeignKey('Country.Country', on_delete=models.PROTECT)
    timezones = models.ManyToManyField('Timezones.TimezoneHandbook', related_name='timezones')
    primary_timezone = models.ForeignKey('Timezones.TimezoneHandbook', on_delete=models.PROTECT,
                                         related_name='primary_timezone')
    currencies = models.ManyToManyField('Currency.Currency', related_name='currencies')
    primary_currency = models.ForeignKey('Currency.Currency', on_delete=models.PROTECT, related_name='primary_currency')

    class Meta:
        db_table = ' clinic_pre_settings'

    def __str__(self):
        return _('Country setting: {country}').format(country=self.country.name)

    def __repr__(self):
        return f'Country ({self.country_id}) setting: {self.id}'

    @property
    def label(self):
        return str(self)

    @classmethod
    def get_setting(cls, country) -> "ClinicPreSettings | None":
        try:
            return cls.objects.active().get(country_id=country.id)
        except ClinicPreSettings.DoesNotExist:
            return None
        except ClinicPreSettings.MultipleObjectsReturned:
            raise ValueError('System incorrectly configured. Returned multiple!')
