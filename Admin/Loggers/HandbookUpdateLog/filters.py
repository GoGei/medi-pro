import django_filters
from core.Loggers.models import HandbookUpdateLog


class HandbookUpdateLogFilter(django_filters.FilterSet):
    class Meta:
        model = HandbookUpdateLog
        fields = ('handbook',)
