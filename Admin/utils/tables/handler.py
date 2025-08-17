from django.conf import settings
from django_tables2 import LazyPaginator, RequestConfig
from Admin.utils.tables.filters import SearchFilter


class TableHandler(object):
    def __init__(self, session_key, request, queryset, table_class, filterset_class=None, search_fields=None):
        table_meta = getattr(table_class, 'Meta', None)

        self.session_key = session_key
        self.request = request
        self.queryset = queryset

        self.table_class = table_class
        self.table = None

        self.filterset_class = filterset_class
        self.filterset = None

        self.search_fields = search_fields
        self.search_class = SearchFilter
        self.searchset = None

        self.ordering = getattr(table_meta, 'ordering_fields', tuple()) if table_meta else tuple()

    def process(self) -> 'TableHandler':
        state = self.request.GET
        qs = self.queryset

        if self.filterset_class:
            self.filterset = self.filterset_class(state, queryset=qs)
            qs = self.filterset.qs

        if self.search_fields:
            self.searchset = self.search_class(state, queryset=qs, search_fields=self.search_fields)
            qs = self.searchset.qs

        if self.ordering:
            qs = qs.order_by(*self.ordering)

        self.table = self.table_class(qs)
        RequestConfig(self.request, paginate={'per_page': settings.ADMIN_PAGINATION_PER_PAGE,
                                              'paginator_class': LazyPaginator}).configure(self.table)
        return self
