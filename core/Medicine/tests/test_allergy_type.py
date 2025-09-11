from django.test import TestCase
from ..models import AllergyType
from ..factories import AllergyTypeFactory


class AllergyTypeTestCase(TestCase):
    def test_create_obj(self):
        obj = AllergyTypeFactory.create()
        self.assertIn(obj, AllergyType.objects.all())
        self.assertTrue(str(obj))
        self.assertTrue(obj.label)

    def test_delete_obj(self):
        obj = AllergyTypeFactory.create()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, AllergyType.objects.all().values_list('id', flat=True))
