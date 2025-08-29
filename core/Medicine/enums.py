from django.db.models import TextChoices
from django.utils.translation import gettext_lazy as _


class MedicineHandbookSources(TextChoices):
    MANUALLY_CREATED = 'manually_created', _('Manually created')
    OTHER = 'other', _('Other')

    # https://www.cms.gov/medicare/coordination-benefits-recovery/overview/icd-code-lists
    CMS_GOV = 'cms.gov', _('CMS.gov')
    HL7 = 'hl7', _('HL7')
