from django.test import TestCase

from ..models import EmployeeColors
from ..factories import EmployeeColorsFactory, DefaultEmployeeColorsFactory


# from ..services import import_countries_from_fixture


class EmployeeColorsTestCase(TestCase):
    def test_create_obj(self):
        obj = EmployeeColorsFactory.create()
        self.assertIn(obj, EmployeeColors.objects.all())

    def test_delete_obj(self):
        obj = EmployeeColorsFactory.create()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, EmployeeColors.objects.all().values_list('id', flat=True))

    def test_default_obj(self):
        obj = EmployeeColorsFactory.create()
        self.assertIsNone(EmployeeColors.get_default())

        EmployeeColors.set_default(obj)
        obj.refresh_from_db()
        self.assertEqual(EmployeeColors.get_default(), obj)

        obj2 = DefaultEmployeeColorsFactory.create()
        self.assertEqual(EmployeeColors.get_default(), obj2)

        EmployeeColorsFactory.create(is_default=True)
        with self.assertRaises(expected_exception=ValueError) as e:
            EmployeeColors.get_default()
        self.assertTrue(e.exception)

    # def test_import_countries_from_fixture(self):
    #     c1 = EmployeeColors.objects.count()
    #     import_countries_from_fixture()
    #     c2 = EmployeeColors.objects.count()
    #     self.assertTrue(c2 > c1)
