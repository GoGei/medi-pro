from django.db import models
from core.Utils.models.mixins import IsActiveMixin


class TimezoneHandbook(IsActiveMixin):
    name = models.CharField(max_length=64, db_index=True)  # initial name from zoneinfo
    offset = models.CharField(max_length=8)
    label = models.CharField(max_length=64)

    class Meta:
        db_table = 'timezone_handbook'
