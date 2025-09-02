import django_filters
from Admin.utils.filters.fields import IsActiveMixinField
from core.Currency.models import Currency


class CurrencyFilter(django_filters.FilterSet):
    is_active = IsActiveMixinField(required=False)

    class Meta:
        model = Currency
        fields = ('is_active',)
