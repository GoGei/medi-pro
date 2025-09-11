from django.test import TestCase
from ..models import PatientRelation
from ..factories import PatientRelationFactory


class PatientRelationTestCase(TestCase):
    def test_create_obj(self):
        obj = PatientRelationFactory.create()
        self.assertIn(obj, PatientRelation.objects.all())
        self.assertTrue(str(obj))
        self.assertTrue(obj.label)

    def test_delete_obj(self):
        obj = PatientRelationFactory.create()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, PatientRelation.objects.all().values_list('id', flat=True))
