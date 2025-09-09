from django.db import models
from django.utils.translation import gettext_lazy as _
from core.Utils.models.mixins import UUIDMixin, IsActiveMixin


class HandbookUpdateLog(UUIDMixin, IsActiveMixin):
    class HandbookChoices(models.TextChoices):
        ALLERGY_TYPE = 'allergy_type', _('Allergy type')
        ALLERGY_CAUSE = 'allergy_cause', _('Allergy cause')
        ALLERGY_REACTION = 'allergy_reaction', _('Allergy reaction')
        ICD_10 = 'icd_10', _('Icd 10')

        TIMEZONE_HANDBOOK = 'timezone_handbook', _('Timezone handbook')
        CURRENCY = 'currency', _('Currency')
        COUNTRIES = 'countries', _('Countries')

        EMPLOYEE_COLOR = 'employee_color', _('Employee color')
        CLINIC_PRE_SETTINGS = 'clinic_pre_settings', _('Clinic pre settings')

    handbook = models.CharField(choices=HandbookChoices.choices, max_length=64)
    user = models.ForeignKey('User.User', on_delete=models.PROTECT, null=True)
    stamp = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'handbook_update_log'
        indexes = [
            models.Index(fields=('handbook', 'stamp'))
        ]

    def __str__(self):
        return f'{self.get_handbook_display()} {self.stamp}'
