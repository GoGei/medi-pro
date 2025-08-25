from django.db import models
from core.Utils.models.mixins import IsActiveMixin


class Country(IsActiveMixin):
    name = models.CharField(max_length=64)
    cca2 = models.CharField(max_length=2, db_index=True, unique=True)
    ccn3 = models.CharField(max_length=3, db_index=True, unique=True)

    class Meta:
        db_table = 'countries'

    @property
    def label(self):
        return self.name