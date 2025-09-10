from django.db import models

from core.Utils.models import fields
from core.Utils.models.mixins import IsActiveMixin


class EmployeeColors(IsActiveMixin):
    name = models.CharField(max_length=64)
    sideline = fields.ColorField()
    background = fields.ColorField()
    is_default = models.BooleanField(default=False, db_index=True)

    class Meta:
        db_table = 'employee_color'

    def __str__(self):
        return self.name

    @property
    def label(self):
        return str(self)

    @classmethod
    def get_default(cls) -> "EmployeeColors | None":
        try:
            return EmployeeColors.objects.active().get(is_default=True)
        except EmployeeColors.DoesNotExist:
            return None
        except EmployeeColors.MultipleObjectsReturned:
            raise ValueError('System incorrectly configured. Returned multiple!')

    @classmethod
    def set_default(cls, obj: "EmployeeColors") -> "EmployeeColors":
        cls.objects.all().update(is_default=False)
        obj.is_default = True
        obj.save(update_fields=['is_default'])
        return obj
