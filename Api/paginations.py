from django.utils.translation import gettext_lazy as _
from rest_framework import pagination
from rest_framework.exceptions import ValidationError


class HardLimitOffsetPagination(pagination.LimitOffsetPagination):
    max_limit_raise = 100

    def paginate_queryset(self, queryset, request, view=None):
        limit = self.get_limit(request)
        if limit > self.max_limit_raise:
            raise ValidationError(
                {'limit': [_('Maximum limit is {max_limit_raise}').format(max_limit_raise=self.max_limit_raise)]})
        return super().paginate_queryset(queryset=queryset, request=request, view=view)


class UnlimitedOffsetPagination(pagination.LimitOffsetPagination):
    def paginate_queryset(self, queryset, request, view=None):
        self.request = request
        self.limit = None
        self.count = self.get_count(queryset)
        self.offset = 0
        return list(queryset)

    def get_next_link(self):
        return None

    def get_previous_link(self):
        return None

    def get_schema_fields(self, view):
        return []

    def get_schema_operation_parameters(self, view):
        return []

    def get_paginated_response_schema(self, schema):
        res = super().get_paginated_response_schema(schema)
        res['properties']['next'] = {'type': 'string', 'nullable': True}
        res['properties']['previous'] = {'type': 'string', 'nullable': True}
        return res
