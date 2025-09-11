from django.db import models
from core.Utils.models.mixins import IsActiveMixin
from .enums import MedicineHandbookSources


class AllergyType(IsActiveMixin):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=16, db_index=True, unique=True)
    source = models.CharField(max_length=64, choices=MedicineHandbookSources.choices,
                              default=MedicineHandbookSources.MANUALLY_CREATED)

    class Meta:
        db_table = 'allergy_type'

    def __str__(self):
        return self.code

    @property
    def label(self):
        return self.code


class AllergyCause(IsActiveMixin):
    name = models.CharField(max_length=128)
    code = models.CharField(max_length=16, db_index=True, unique=True)
    source = models.CharField(max_length=64, choices=MedicineHandbookSources.choices,
                              default=MedicineHandbookSources.MANUALLY_CREATED)

    class Meta:
        db_table = 'allergy_cause'

    def __str__(self):
        return self.code

    @property
    def label(self):
        return self.code


class AllergyReaction(IsActiveMixin):
    name = models.CharField(max_length=512)
    code = models.CharField(max_length=16, db_index=True, unique=True)
    source = models.CharField(max_length=64, choices=MedicineHandbookSources.choices,
                              default=MedicineHandbookSources.MANUALLY_CREATED)

    class Meta:
        db_table = 'allergy_reaction'

    def __str__(self):
        return self.code

    @property
    def label(self):
        return self.code


class ICD10(IsActiveMixin):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=16, db_index=True, unique=True)
    source = models.CharField(max_length=64, choices=MedicineHandbookSources.choices,
                              default=MedicineHandbookSources.MANUALLY_CREATED)

    class Meta:
        db_table = 'icd_10'

    def __str__(self):
        return self.code

    @property
    def label(self):
        return self.code


class PatientRelation(IsActiveMixin):
    name = models.CharField(max_length=64)

    class Meta:
        db_table = 'patient_relation'

    def __str__(self):
        return self.name

    @property
    def label(self):
        return self.name
