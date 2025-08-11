from django.utils import timezone
from factory import fuzzy, Faker
from factory.django import DjangoModelFactory

from core.User.models import User


class UserFactory(DjangoModelFactory):
    class Meta:
        model = User
        django_get_or_create = ('email',)

    email = Faker('email')
    is_staff = False
    is_superuser = False
    is_active = True

    date_joined = fuzzy.FuzzyDateTime(start_dt=timezone.now())
    last_login = fuzzy.FuzzyDateTime(start_dt=timezone.now())
    first_name = fuzzy.FuzzyText(length=50)
    last_name = fuzzy.FuzzyText(length=50)


class StaffUserFactory(UserFactory):
    is_staff = True


class SuperUserFactory(UserFactory):
    is_staff = True
    is_superuser = True
