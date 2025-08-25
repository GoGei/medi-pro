from django.test import TestCase
from ..models import Country
from ..factories import CountryFactory


class CountryTestCase(TestCase):
    def test_create_obj(self):
        obj = CountryFactory()
        self.assertIn(obj, Country.objects.all())

    def test_delete_obj(self):
        obj = CountryFactory()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, Country.objects.all().values_list('id', flat=True))
