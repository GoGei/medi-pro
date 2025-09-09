from django.test import TestCase

from core.Country.factories import CountryFactory
from core.Currency.factories import CurrencyFactory
from core.Timezones.factories import TimezoneHandbookFactory
from ..models import ClinicPreSettings
from ..factories import ClinicPreSettingsFactory
from ..services import LoadClinicPreSettingsException, import_clinic_pre_settings


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

        data_item = {
            'country_ccn3': country.ccn3,
            'timezone_name': primary_timezone.name,
            'currency_code': primary_currency.code,
            'timezone_names': [x.name for x in timezones],
            'currency_codes': [x.code for x in currencies],
        }
        data = [data_item]

        items = import_clinic_pre_settings(data=data)
        self.assertEqual(len(items), len(data))

        item = items[0]
        self.assertEqual(item.country_id, country.id)
        self.assertEqual(item.timezones.all().count(), len(timezones))
        self.assertEqual(item.primary_timezone_id, primary_timezone.id)
        self.assertEqual(item.currencies.all().count(), len(currencies))
        self.assertEqual(item.primary_currency_id, primary_currency.id)

        data = [data_item, data_item]
        with self.assertRaises(expected_exception=LoadClinicPreSettingsException) as e:
            import_clinic_pre_settings(data=data)
        self.assertIn(country.ccn3, str(e.exception))
        self.assertIn(country.name, str(e.exception))

    def test_import_clinic_pre_settings_exceptions(self):
        country = CountryFactory.create()
        primary_timezone = TimezoneHandbookFactory.create()
        primary_currency = CurrencyFactory.create()

        data_item = {
            'country_ccn3': country.ccn3,
            'timezone_name': primary_timezone.name,
            'currency_code': primary_currency.code,
            'timezone_names': 'unknown',
            'currency_codes': 'unknown',
        }
        with self.assertRaises(expected_exception=LoadClinicPreSettingsException) as e:
            import_clinic_pre_settings(data=[data_item])
        self.assertIn(data_item['timezone_names'], str(e.exception))

        data_item['timezone_names'] = primary_timezone.name
        with self.assertRaises(expected_exception=LoadClinicPreSettingsException) as e:
            import_clinic_pre_settings(data=[data_item])
        self.assertIn(data_item['currency_codes'], str(e.exception))

    def test_get_setting(self):
        country = CountryFactory.create()
        self.assertIsNone(ClinicPreSettings.get_setting(country))

        obj = ClinicPreSettingsFactory.create(country=country)
        self.assertEqual(ClinicPreSettings.get_setting(country), obj)

        ClinicPreSettingsFactory.create(country=country)
        with self.assertRaises(expected_exception=ValueError) as e:
            ClinicPreSettings.get_setting(country)
        self.assertTrue(e.exception)
