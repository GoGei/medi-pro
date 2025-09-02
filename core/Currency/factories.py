import string

from factory import fuzzy
from factory.django import DjangoModelFactory
from .models import Currency


class CurrencyFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=64)
    code = fuzzy.FuzzyText(length=3, chars=string.ascii_uppercase)
    symbol = fuzzy.FuzzyText(length=4, chars=string.ascii_uppercase)

    class Meta:
        model = Currency
