from factory import SubFactory, post_generation
from factory.django import DjangoModelFactory
from .models import ClinicPreSettings


class ClinicPreSettingsFactory(DjangoModelFactory):
    country = SubFactory('core.Country.factories.CountryFactory')
    primary_timezone = SubFactory('core.Timezones.factories.TimezoneHandbookFactory')
    primary_currency = SubFactory('core.Currency.factories.CurrencyFactory')

    @post_generation
    def timezones(self, create, extracted, **kwargs):
        if not create:
            return
        for item in extracted or list():
            self.timezones.add(item)

    @post_generation
    def currencies(self, create, extracted, **kwargs):
        if not create:
            return
        for item in extracted or list():
            self.currencies.add(item)

    class Meta:
        model = ClinicPreSettings
