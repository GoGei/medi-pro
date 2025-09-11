from django.test import TestCase
from ..models import EmployeeRole
from ..factories import EmployeeRoleFactory


class EmployeeRoleTestCase(TestCase):
    def test_create_obj(self):
        obj = EmployeeRoleFactory.create()
        self.assertIn(obj, EmployeeRole.objects.all())
        self.assertTrue(str(obj))
        self.assertTrue(obj.label)

    def test_delete_obj(self):
        obj = EmployeeRoleFactory.create()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, EmployeeRole.objects.all().values_list('id', flat=True))

    def test_archive_obj(self):
        obj = EmployeeRoleFactory.create()
        with self.assertRaises(ValueError):
            obj.archive()

        obj2 = EmployeeRoleFactory.create(slug='test')
        obj2 = obj2.archive()
        self.assertFalse(obj2.is_active)
