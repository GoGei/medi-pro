import django_filters
from Admin.utils.filters.fields import IsActiveMixinField
from core.Medicine.models import PatientRelation


class PatientRelationFilter(django_filters.FilterSet):
    is_active = IsActiveMixinField(required=False)

    class Meta:
        model = PatientRelation
        fields = ('is_active',)
