from django.conf import settings
from django_tables2 import LazyPaginator, RequestConfig


class TableHandler(object):
    def __init__(self, session_key, request, queryset, table_class, filterset_class=None, ordering=None):
        table_meta = getattr(table_class, 'Meta', None)

        self.session_key = session_key
        self.request = request
        self.queryset = queryset
        self.table_class = table_class
        self.filterset_class = filterset_class
        self.ordering = getattr(table_meta, 'ordering_fields', tuple()) if table_meta else tuple()
        self.filterset = None
        self.table = None

    def _get_state_from_request(self):
        if self.request.GET:
            state = self.request.GET.dict()
            self.request.session[self.session_key] = state
            return state
        return self.request.session.get(self.session_key, {})

    def process(self):
        state = self._get_state_from_request()
        qs = self.queryset

        if self.filterset_class:
            self.filterset = self.filterset_class(state, queryset=qs)
            qs = self.filterset.qs

        if self.ordering:
            qs = qs.order_by(*self.ordering)

        self.table = self.table_class(qs)
        RequestConfig(self.request, paginate={'per_page': settings.ADMIN_PAGINATION_PER_PAGE,
                                              'paginator_class': LazyPaginator}).configure(self.table)
        return self.table, self.filterset
