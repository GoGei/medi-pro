from django.test import TestCase

from ..models import EmployeeColors
from ..factories import EmployeeColorsFactory, DefaultEmployeeColorsFactory
from ..services import LocaColorsException, import_colors_from_fixture


class EmployeeColorsTestCase(TestCase):
    def test_create_obj(self):
        obj = EmployeeColorsFactory.create()
        self.assertIn(obj, EmployeeColors.objects.all())
        self.assertTrue(str(obj))
        self.assertTrue(obj.label)

    def test_delete_obj(self):
        obj = EmployeeColorsFactory.create()
        obj_id = obj.id
        obj.delete()
        self.assertNotIn(obj_id, EmployeeColors.objects.all().values_list('id', flat=True))

    def test_default_obj(self):
        obj = EmployeeColorsFactory.create()
        self.assertIsNone(EmployeeColors.get_default())

        EmployeeColors.set_default(obj)
        obj.refresh_from_db()
        self.assertEqual(EmployeeColors.get_default(), obj)

        obj2 = DefaultEmployeeColorsFactory.create()
        self.assertEqual(EmployeeColors.get_default(), obj2)

        EmployeeColorsFactory.create(is_default=True)
        with self.assertRaises(expected_exception=ValueError) as e:
            EmployeeColors.get_default()
        self.assertTrue(e.exception)

    def test_import_colors_from_fixture(self):
        archived_color = EmployeeColorsFactory.create()
        archived_color.archive()

        c1 = EmployeeColors.objects.count()
        import_colors_from_fixture()
        c2 = EmployeeColors.objects.count()
        self.assertEqual(c2, c1 + 16)

        data = [
            {
                "name": "Tomato",
                "sideline": "#aaaaaa",
                "background": "#aaaaaa",
                "is_default": False
            },
            {
                "name": "Tangerine",
                "sideline": "#ffffff",
                "background": "#ffffff",
                "is_default": False
            },
            {
                "name": "Test",
                "sideline": archived_color.sideline,
                "background": "#ffffff",
                "is_default": False
            }
        ]
        import_colors_from_fixture(data=data)
        c3 = EmployeeColors.objects.count()
        self.assertEqual(c3, c2 + 2)

    def test_import_colors_from_fixture_validate_2_default_provided(self):
        data = [
            {
                "name": "Tomato",
                "sideline": "#aaaaaa",
                "background": "#aaaaaa",
                "is_default": True
            },
            {
                "name": "Tangerine",
                "sideline": "#ffffff",
                "background": "#ffffff",
                "is_default": True
            }
        ]

        with self.assertRaises(LocaColorsException) as e:
            import_colors_from_fixture(data=data)
        self.assertTrue(e.exception)

    def test_import_colors_from_fixture_validate_color_regex(self):
        data = [
            {
                "name": "Tomato",
                "sideline": "#sideline",
                "background": "#aaaaaa",
                "is_default": True
            }
        ]

        with self.assertRaises(LocaColorsException) as e:
            import_colors_from_fixture(data=data)
        self.assertIn('SIDELINE', str(e.exception))

        data = [
            {
                "name": "Tomato",
                "sideline": "#aaaaaa",
                "background": "#background",
                "is_default": True
            }
        ]

        with self.assertRaises(LocaColorsException) as e:
            import_colors_from_fixture(data=data)
        self.assertIn('BACKGROUND', str(e.exception))
