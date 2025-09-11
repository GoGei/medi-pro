from django.test import TestCase
from ..models import AllergyCause
from ..factories import AllergyCauseFactory


class AllergyCauseTestCase(TestCase):
    def test_create_obj(self):
        obj = AllergyCauseFactory.create()
        self.assertIn(obj, AllergyCause.objects.all())
        self.assertTrue(str(obj))
        self.assertTrue(obj.label)

    def test_delete_obj(self):
        obj = AllergyCauseFactory.create()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, AllergyCause.objects.all().values_list('id', flat=True))
