from django.test import TestCase
from ..models import ICD10
from ..factories import ICD10Factory


class ICD10TestCase(TestCase):
    def test_create_obj(self):
        obj = ICD10Factory.create()
        self.assertIn(obj, ICD10.objects.all())
        self.assertTrue(str(obj))
        self.assertTrue(obj.label)

    def test_delete_obj(self):
        obj = ICD10Factory.create()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, ICD10.objects.all().values_list('id', flat=True))
