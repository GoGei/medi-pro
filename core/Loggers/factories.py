from factory import SubFactory, fuzzy
from factory.django import DjangoModelFactory
from .models import HandbookUpdateLog


class HandbookUpdateLogFactory(DjangoModelFactory):
    class Meta:
        model = HandbookUpdateLog

    handbook = fuzzy.FuzzyChoice(dict(HandbookUpdateLog.HandbookChoices.choices).keys())
    user = SubFactory('core.User.factories.UserFactory')
