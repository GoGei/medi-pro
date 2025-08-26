from factory import fuzzy
from factory.django import DjangoModelFactory
from .enums import MedicineHandbookSources
from .models import (
    AllergyType, AllergyCause, AllergyReaction, ICD10, PatientRelation
)


class AllergyTypeFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=64)
    code = fuzzy.FuzzyText(length=8)
    source = fuzzy.FuzzyChoice(choices=dict(MedicineHandbookSources.choices).keys())

    class Meta:
        model = AllergyType
        django_get_or_create = ('code',)


class AllergyCauseFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=64)
    code = fuzzy.FuzzyText(length=8)
    source = fuzzy.FuzzyChoice(choices=dict(MedicineHandbookSources.choices).keys())

    class Meta:
        model = AllergyCause
        django_get_or_create = ('code',)


class AllergyReactionFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=64)
    code = fuzzy.FuzzyText(length=8)
    source = fuzzy.FuzzyChoice(choices=dict(MedicineHandbookSources.choices).keys())

    class Meta:
        model = AllergyReaction
        django_get_or_create = ('code',)


class ICD10Factory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=64)
    code = fuzzy.FuzzyText(length=8)
    source = fuzzy.FuzzyChoice(choices=dict(MedicineHandbookSources.choices).keys())

    class Meta:
        model = ICD10
        django_get_or_create = ('code',)


class PatientRelationFactory(DjangoModelFactory):
    name = fuzzy.FuzzyText(length=64)

    class Meta:
        model = PatientRelation
