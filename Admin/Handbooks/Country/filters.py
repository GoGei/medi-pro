import django_filters
from Admin.utils.filters.fields import IsActiveMixinField
from core.Country.models import Country


class CountryFilter(django_filters.FilterSet):
    is_active = IsActiveMixinField(required=False)

    class Meta:
        model = Country
        fields = ('is_active',)
