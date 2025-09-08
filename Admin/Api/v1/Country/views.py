from Api.filters import CustomSearchFilter, CustomOrderingFilter
from Api.permissions import AdminPermissions
from Api.views.mixins import CrmListModelMixin

from core.Country.models import Country
from .serializers import CountrySerializer


class CountryViewSet(CrmListModelMixin):
    permission_classes = (AdminPermissions,)
    queryset = Country.objects.active().order_by('name')
    serializer_class = CountrySerializer

    filter_backends = (CustomSearchFilter, CustomOrderingFilter)
    search_fields = ('^name', '=cca2', '=ccn3')
    ordering_fields = ('name',)
