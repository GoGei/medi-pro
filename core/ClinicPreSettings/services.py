from django.utils.translation import gettext_lazy as _
from core.Country.models import Country
from core.Currency.models import Currency
from core.Timezones.models import TimezoneHandbook
from .models import ClinicPreSettings


class LoadClinicPreSettingsException(Exception):
    pass


def import_clinic_pre_settings(data: list[dict]) -> list[ClinicPreSettings]:
    ClinicPreSettings.objects.all().archive()
    items: list[ClinicPreSettings] = list()

    countries_qs = Country.objects.active()
    timezones_qs = TimezoneHandbook.objects.active()
    currencies_qs = Currency.objects.active()

    setup_country = set()

    for item in data:
        country = countries_qs.get(ccn3=item['country_ccn3'])
        if country.id in setup_country:
            msg = _('In data country {name} ({code}) mentioned more than 1 time: {item}').format(name=country.name,
                                                                                                 code=country.ccn3,
                                                                                                 item=str(item))
            raise LoadClinicPreSettingsException(msg)
        else:
            setup_country.add(country.id)

        primary_timezone = timezones_qs.get(name=item['timezone_name'])
        primary_currency = currencies_qs.get(code=item['currency_code'])

        timezone_names = item['timezone_names']
        timezones = timezones_qs.filter(name__in=timezone_names)
        if timezones.count() != len(timezone_names):
            msg = _('Not all timezones found in item: {item}. Expected: {expected}. Found: {found}').format(
                item=str(item),
                expected=', '.join(timezone_names),
                found=', '.join(timezones.values_list('name', flat=True)))
            raise LoadClinicPreSettingsException(msg)

        currency_codes = item['currency_codes']
        currencies = currencies_qs.filter(code__in=currency_codes)
        if currencies.count() != len(currency_codes):
            msg = _('Not all currencies found in item: {item}. Expected: {expected}. Found: {found}').format(
                item=str(item),
                expected=', '.join(currency_codes),
                found=', '.join(currencies.values_list('code', flat=True)))
            raise LoadClinicPreSettingsException(msg)

        setting = ClinicPreSettings.objects.create(
            country=country,
            primary_timezone=primary_timezone,
            primary_currency=primary_currency,
        )
        setting.timezones.set(timezones)
        setting.currencies.set(currencies)
        items.append(setting)
    return items
