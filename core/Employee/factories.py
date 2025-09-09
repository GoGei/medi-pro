from factory import fuzzy
from factory.django import DjangoModelFactory
from .models import EmployeeRole


class EmployeeRoleFactory(DjangoModelFactory):
    class Meta:
        model = EmployeeRole
        django_get_or_create = ('slug',)

    slug = fuzzy.FuzzyChoice(dict(EmployeeRole.EmployeeRoleSlugs.choices).keys())
    name = fuzzy.FuzzyText(length=128)
