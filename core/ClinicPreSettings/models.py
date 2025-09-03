from django.db import models
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
