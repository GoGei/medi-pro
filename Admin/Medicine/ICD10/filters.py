import django_filters
from Admin.utils.filters.fields import IsActiveMixinField
from core.Medicine.models import ICD10


class ICD10Filter(django_filters.FilterSet):
    is_active = IsActiveMixinField(required=False)

    class Meta:
        model = ICD10
        fields = ('is_active', 'source')
