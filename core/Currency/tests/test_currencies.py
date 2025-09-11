from django.test import TestCase

from ..models import Currency
from ..factories import CurrencyFactory
from ..services import LoadCurrenciesException, import_currencies_from_fixture


class CurrencyTestCase(TestCase):
    def test_create_obj(self):
        obj = CurrencyFactory.create()
        self.assertIn(obj, Currency.objects.all())
        self.assertTrue(str(obj))
        self.assertTrue(obj.label)

    def test_delete_obj(self):
        obj = CurrencyFactory.create()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, Currency.objects.all().values_list('id', flat=True))

    def test_import_currencies_from_fixture(self):
        archived_currency = CurrencyFactory.create()
        archived_currency.archive()

        c1 = Currency.objects.count()
        import_currencies_from_fixture()
        c2 = Currency.objects.count()
        self.assertEqual(c2, c1 + 118)

        data = [
            {
                "symbol": "$",
                "name": "Test1",
                "symbol_native": "$",
                "code": "T1",
            },
            {
                "symbol": "$",
                "name": "Test2",
                "symbol_native": "$",
                "code": "T2",
            },
            {
                "symbol": "$",
                "name": "Test3",
                "symbol_native": "$",
                "code": archived_currency.code,
            },
        ]
        import_currencies_from_fixture(data=data)
        c3 = Currency.objects.count()
        self.assertEqual(c3, c2 + 2)

        archived_currency.refresh_from_db()
        self.assertTrue(archived_currency.is_active)

    def test_import_currencies_from_fixture_validate_same_code(self):
        data = [
            {
                "symbol": "$",
                "name": "Test1",
                "symbol_native": "$",
                "code": "T1",
            },
            {
                "symbol": "$",
                "name": "Test2",
                "symbol_native": "$",
                "code": "T1",
            },
        ]
        with self.assertRaises(LoadCurrenciesException) as e:
            import_currencies_from_fixture(data=data)
        self.assertIn('codes', str(e.exception))
