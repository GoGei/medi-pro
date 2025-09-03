from django.test import TestCase

from core.Country.factories import CountryFactory
from core.Currency.factories import CurrencyFactory
from core.Timezones.factories import TimezoneHandbookFactory
from ..models import ClinicPreSettings
from ..factories import ClinicPreSettingsFactory
from ..services import import_clinic_pre_settings


class ClinicPreSettingsTestCase(TestCase):
    def test_create_obj(self):
        obj = ClinicPreSettingsFactory.create()
        self.assertIn(obj, ClinicPreSettings.objects.all())

    def test_delete_obj(self):
        obj = ClinicPreSettingsFactory.create()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, ClinicPreSettings.objects.all().values_list('id', flat=True))

    def test_import_clinic_pre_settings(self):
        country = CountryFactory.create()
        timezones = TimezoneHandbookFactory.create_batch(size=3)
        primary_timezone = TimezoneHandbookFactory.create()
        currencies = CurrencyFactory.create_batch(size=3)
        primary_currency = CurrencyFactory.create()

        data = [
            {
                'country_ccn3': country.ccn3,
                'timezone_name': primary_timezone.name,
                'currency_code': primary_currency.code,
                'timezone_names': ','.join([x.name for x in timezones]),
                'currency_codes': ','.join([x.code for x in currencies]),
            }
        ]

        items = import_clinic_pre_settings(data=data)
        self.assertEqual(len(items), len(data))

        item = items[0]
        self.assertEqual(item.country_id, country.id)
        self.assertEqual(item.timezones.all().count(), len(timezones))
        self.assertEqual(item.primary_timezone_id, primary_timezone.id)
        self.assertEqual(item.currencies.all().count(), len(currencies))
        self.assertEqual(item.primary_currency_id, primary_currency.id)
