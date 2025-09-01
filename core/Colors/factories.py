from factory import fuzzy
from factory.base import T
from factory.django import DjangoModelFactory
from core.Utils.test.fuzzy import FuzzyColor
from .models import EmployeeColors


class EmployeeColorsFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=64)
    sideline = FuzzyColor()
    background = FuzzyColor()
    is_default = False

    class Meta:
        model = EmployeeColors


class DefaultEmployeeColorsFactory(EmployeeColorsFactory):
    is_default = True

    @classmethod
    def create(cls, **kwargs) -> T:
        obj = super().create(**kwargs)
        EmployeeColors.set_default(obj)
        return obj
