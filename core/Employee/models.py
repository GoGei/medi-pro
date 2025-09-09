from django.db import models
from django.utils.translation import gettext_lazy as _
from core.Utils.models.mixins import IsActiveMixin


class EmployeeRole(IsActiveMixin):
    class EmployeeRoleSlugs(models.TextChoices):
        ADMIN = 'admin', _('Administrator')
        DOCTOR = 'doctor', _('Doctor')
        OWNER = 'owner', _('Owner')

    slug = models.SlugField(choices=EmployeeRoleSlugs.choices, unique=True)
    name = models.CharField(max_length=128)

    class Meta:
        db_table = 'employee_role'

    def __str__(self):
        return self.name

    @property
    def label(self):
        return str(self)

    def archive(self, *args, **kwargs):
        if self.slug in self.EmployeeRoleSlugs:
            raise ValueError('Unable to archive default employee role')
        return super().archive(*args, **kwargs)
