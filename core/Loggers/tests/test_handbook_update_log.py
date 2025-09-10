from django.test import TestCase
from ..models import HandbookUpdateLog
from ..factories import HandbookUpdateLogFactory


class HandbookUpdateLogTestCase(TestCase):
    def test_create_obj(self):
        obj = HandbookUpdateLogFactory.create()
        self.assertIn(obj, HandbookUpdateLog.objects.all())

    def test_delete_obj(self):
        obj = HandbookUpdateLogFactory.create()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, HandbookUpdateLog.objects.all().values_list('id', flat=True))
