import django_filters
from django.db.models import Q
from django.utils.translation import gettext_lazy as _


class SearchFilter(django_filters.FilterSet):
    LOOKUP_SEP = '__'
    default_prefix = 'icontains'
    lookup_prefixes = {
        '^': 'istartswith',
        '=': 'iexact',
        '$': 'iregex',
        '@': 'search',
    }

    search = django_filters.CharFilter(method='filter_search', label=_('Search'))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        meta = getattr(self, 'Meta', None)
        self.search_fields = getattr(meta, 'search_fields', tuple())

    def filter_search(self, queryset, name, value):
        q = Q()
        for field_name in self.search_fields:
            lookup = self.lookup_prefixes.get(field_name[0])
            if lookup:
                field_name = field_name[1:]
            else:
                lookup = self.default_prefix

            field = self.LOOKUP_SEP.join([field_name, lookup])
            q |= Q(**{field: value})
        return queryset.filter(q)
