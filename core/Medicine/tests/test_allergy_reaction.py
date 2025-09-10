from django.test import TestCase
from ..models import AllergyReaction
from ..factories import AllergyReactionFactory


class AllergyReactionTestCase(TestCase):
    def test_create_obj(self):
        obj = AllergyReactionFactory.create()
        self.assertIn(obj, AllergyReaction.objects.all())

    def test_delete_obj(self):
        obj = AllergyReactionFactory.create()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, AllergyReaction.objects.all().values_list('id', flat=True))
