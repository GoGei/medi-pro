import django_filters
from Admin.utils.filters.fields import IsActiveMixinField
from core.Medicine.models import AllergyType


class AllergyTypeFilter(django_filters.FilterSet):
    is_active = IsActiveMixinField(required=False)

    class Meta:
        model = AllergyType
        fields = ('is_active', 'source')
