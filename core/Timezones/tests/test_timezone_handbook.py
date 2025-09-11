from django.test import TestCase
from ..models import TimezoneHandbook
from ..factories import TimezoneHandbookFactory
from ..services import LoadTimezonesException, import_timezones, load_timezones


class TimezoneHandbookTestCase(TestCase):
    def test_create_obj(self):
        obj = TimezoneHandbookFactory.create()
        self.assertIn(obj, TimezoneHandbook.objects.all())
        self.assertTrue(str(obj))

    def test_delete_obj(self):
        obj = TimezoneHandbookFactory.create()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, TimezoneHandbook.objects.all().values_list('id', flat=True))

    def test_import_timezones(self):
        archived_timezone = TimezoneHandbookFactory.create(name='UTC')
        archived_timezone.archive()

        c1 = TimezoneHandbook.objects.count()
        import_timezones()
        c2 = TimezoneHandbook.objects.count()
        self.assertEqual(c2, c1 + 598)

        archived_timezone.refresh_from_db()
        self.assertTrue(archived_timezone.is_active)

    def test_load_timezones(self):
        archived_timezone = TimezoneHandbookFactory.create()
        archived_timezone.archive()
        c1 = TimezoneHandbook.objects.count()
        load_timezones(data=[
            {'name': 'test', 'offset': '00:00', 'label': 'Test'},
            {'name': archived_timezone.name, 'offset': '00:00', 'label': 'Test'}
        ])
        c2 = TimezoneHandbook.objects.count()
        self.assertEqual(c2, c1 + 1)

        archived_timezone.refresh_from_db()
        self.assertTrue(archived_timezone.is_active)

    def test_load_timezones_run_validation(self):
        with self.assertRaises(LoadTimezonesException) as e:
            load_timezones(data=[
                {'name': 'test', 'offset': '00:00', 'label': 'Test'},
                {'name': 'test', 'offset': '00:00', 'label': 'Test'}
            ])
        self.assertIn('Duplicated names presented', str(e.exception))
