from rest_framework import serializers
from core.Currency.models import Currency


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = (
            'id',
            'is_active',
            'name',
            'code',
            'label',
        )
