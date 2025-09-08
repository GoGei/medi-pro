from rest_framework import serializers
from core.Timezones.models import TimezoneHandbook


class TimezoneHandbookSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimezoneHandbook
        fields = (
            'id',
            'is_active',
            'name',
            'offset',
            'label',
        )
