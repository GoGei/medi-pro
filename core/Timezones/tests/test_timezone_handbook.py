from django.test import TestCase
from ..models import TimezoneHandbook
from ..factories import TimezoneHandbookFactory
from ..services import import_timezones, load_timezones


class TimezoneHandbookTestCase(TestCase):
    def test_create_obj(self):
        obj = TimezoneHandbookFactory()
        self.assertIn(obj, TimezoneHandbook.objects.all())

    def test_delete_obj(self):
        obj = TimezoneHandbookFactory()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, TimezoneHandbook.objects.all().values_list('id', flat=True))

    def test_import_timezones(self):
        c1 = TimezoneHandbook.objects.count()
        import_timezones()
        c2 = TimezoneHandbook.objects.count()
        self.assertTrue(c2 > c1)

    def test_load_timezones(self):
        c1 = TimezoneHandbook.objects.count()
        load_timezones(data=[{'name': 'test', 'offset': '00:00', 'label': 'Test'}], archive_not_mentioned=False)
        c2 = TimezoneHandbook.objects.count()
        self.assertTrue(c2 > c1)
