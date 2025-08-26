from django.db import models
from core.Utils.models.mixins import IsActiveMixin
from .enums import MedicineHandbookSources


class AllergyType(IsActiveMixin):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=8, db_index=True, unique=True)
    source = models.CharField(max_length=64, choices=MedicineHandbookSources.choices,
                              default=MedicineHandbookSources.MANUALLY_CREATED)

    class Meta:
        db_table = 'allergy_type'

    @property
    def label(self):
        return self.name


class AllergyCause(IsActiveMixin):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=8, db_index=True, unique=True)
    source = models.CharField(max_length=64, choices=MedicineHandbookSources.choices,
                              default=MedicineHandbookSources.MANUALLY_CREATED)

    class Meta:
        db_table = 'allergy_cause'

    @property
    def label(self):
        return self.name


class AllergyReaction(IsActiveMixin):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=8, db_index=True, unique=True)
    source = models.CharField(max_length=64, choices=MedicineHandbookSources.choices,
                              default=MedicineHandbookSources.MANUALLY_CREATED)

    class Meta:
        db_table = 'allergy_reaction'

    @property
    def label(self):
        return self.name


class ICD10(IsActiveMixin):
    name = models.CharField(max_length=64)
    code = models.CharField(max_length=8, db_index=True, unique=True)
    source = models.CharField(max_length=64, choices=MedicineHandbookSources.choices,
                              default=MedicineHandbookSources.MANUALLY_CREATED)

    class Meta:
        db_table = 'icd_10'

    @property
    def label(self):
        return self.name


class PatientRelation(IsActiveMixin):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'patient_relation'

    @property
    def label(self):
        return self.name
