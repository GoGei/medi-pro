from django.test import TestCase

from ..models import ClinicPreSettings
from ..factories import ClinicPreSettingsFactory


class ClinicPreSettingsTestCase(TestCase):
    def test_create_obj(self):
        obj = ClinicPreSettingsFactory.create()
        self.assertIn(obj, ClinicPreSettings.objects.all())

    def test_delete_obj(self):
        obj = ClinicPreSettingsFactory.create()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, ClinicPreSettings.objects.all().values_list('id', flat=True))
