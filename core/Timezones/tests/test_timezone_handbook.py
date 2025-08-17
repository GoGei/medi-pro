from django.test import TestCase
from ..models import TimezoneHandbook
from ..factories import TimezoneHandbookFactory


class TimezoneHandbookTestCase(TestCase):
    def test_create_obj(self):
        obj = TimezoneHandbookFactory()
        self.assertIn(obj, TimezoneHandbook.objects.all())

    def test_delete_obj(self):
        obj = TimezoneHandbookFactory()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, TimezoneHandbook.objects.all().values_list('id', flat=True))
