from Api.filters import CustomSearchFilter, CustomOrderingFilter
from Api.permissions import AdminPermissions
from Api.views.mixins import CrmListModelMixin

from core.Timezones.models import TimezoneHandbook
from .serializers import TimezoneHandbookSerializer


class TimezoneHandbookViewSet(CrmListModelMixin):
    permission_classes = (AdminPermissions,)
    queryset = TimezoneHandbook.objects.active().order_by('name')
    serializer_class = TimezoneHandbookSerializer

    filter_backends = (CustomSearchFilter, CustomOrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name',)
