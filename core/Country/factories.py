import string

from factory import fuzzy
from factory.django import DjangoModelFactory

from .models import Country


class CountryFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=64)
    cca2 = fuzzy.FuzzyText(length=2, chars=string.ascii_uppercase)
    ccn3 = fuzzy.FuzzyText(length=3, chars=string.digits)

    class Meta:
        model = Country
        django_get_or_create = ('ccn3', 'cca2')
