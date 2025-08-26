import django_filters
from Admin.utils.filters.fields import IsActiveMixinField
from core.Medicine.models import AllergyCause


class AllergyCauseFilter(django_filters.FilterSet):
    is_active = IsActiveMixinField(required=False)

    class Meta:
        model = AllergyCause
        fields = ('is_active', 'source')
