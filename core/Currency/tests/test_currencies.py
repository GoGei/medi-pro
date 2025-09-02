from django.test import TestCase

from ..models import Currency
from ..factories import CurrencyFactory
from ..services import import_currencies_from_fixture


class CurrencyTestCase(TestCase):
    def test_create_obj(self):
        obj = CurrencyFactory.create()
        self.assertIn(obj, Currency.objects.all())

    def test_delete_obj(self):
        obj = CurrencyFactory.create()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, Currency.objects.all().values_list('id', flat=True))

    def test_import_colors_from_fixture(self):
        c1 = Currency.objects.count()
        import_currencies_from_fixture()
        c2 = Currency.objects.count()
        self.assertTrue(c2 > c1)
