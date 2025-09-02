from django.db import models

from core.Utils.models.mixins import IsActiveMixin


class Currency(IsActiveMixin):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=3)
    symbol = models.CharField(max_length=8)

    class Meta:
        db_table = 'currency'

    def __str__(self):
        return self.name

    @property
    def label(self):
        return str(self)
