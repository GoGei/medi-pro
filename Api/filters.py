from django.utils.encoding import force_str
from rest_framework.filters import SearchFilter, OrderingFilter
from django.utils.translation import gettext_lazy as _


class CustomSearchFilter(SearchFilter):
    search_description = _('A search term. Search by: %s')

    def get_schema_fields(self, view):
        return super().get_schema_fields(view)

    def get_schema_operation_parameters(self, view):
        res = super().get_schema_operation_parameters(view)
        res[0]['description'] = force_str(self.search_description % ', '.join(view.search_fields))
        return res


class CustomOrderingFilter(OrderingFilter):
    ordering_description = _('Which field to use when ordering the results. Order by: %s')

    def get_schema_fields(self, view):
        return super().get_schema_fields(view)

    def get_schema_operation_parameters(self, view):
        res = super().get_schema_operation_parameters(view)
        res[0]['description'] = force_str(self.ordering_description % ', '.join(view.ordering_fields))
        return res
