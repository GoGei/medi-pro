from django.test import TestCase
from faker import Faker
from ..models import User
from ..factories import UserFactory
from core.Utils.test.fuzzy import FuzzyPassword

fake = Faker()


class UserTestCase(TestCase):
    def test_create_user(self):
        user = UserFactory()
        self.assertIn(user, User.objects.all())

    def test_delete_user(self):
        user = UserFactory()
        user_id = user.id
        user.delete()
        self.assertNotIn(user_id, User.objects.all().values_list('id', flat=True))

    def test_create_user_empty_email(self):
        user = UserFactory(email='')
        self.assertIsNone(user.email)

    def test_manager_create_user(self):
        user = User.objects.create_user(email=fake.email(),
                                        password=FuzzyPassword().fuzz())
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password=FuzzyPassword().fuzz())
            User.objects.create_user(email=fake.email(), password=FuzzyPassword().fuzz(), is_staff=True)
            User.objects.create_user(email=fake.email(), password=FuzzyPassword().fuzz(), is_superuser=True)

    def test_manager_create_superuser(self):
        user = User.objects.create_superuser(email=fake.email(),
                                             password=FuzzyPassword().fuzz())
        self.assertTrue(user.is_active)
        self.assertTrue(user.is_staff)
        self.assertTrue(user.is_superuser)

        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password=FuzzyPassword().fuzz())
            User.objects.create_user(email=fake.email(), password=FuzzyPassword().fuzz(), is_staff=False)
            User.objects.create_user(email=fake.email(), password=FuzzyPassword().fuzz(), is_superuser=False)

    def test_hash_id(self):
        user = UserFactory()
        self.assertEqual(user, User.get_by_hashid(user.hashid()))

        values = User.decode(user.hashid())
        self.assertEqual(user.id, values[0])
