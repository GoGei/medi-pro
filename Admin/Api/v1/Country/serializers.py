from rest_framework import serializers
from core.Country.models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = (
            'id',
            'name',
            'ccn3',
            'cca2',
            'label',
        )
