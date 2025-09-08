from Api.filters import CustomSearchFilter, CustomOrderingFilter
from Api.permissions import AdminPermissions
from Api.views.mixins import CrmListModelMixin

from core.Currency.models import Currency
from .serializers import CurrencySerializer


class CurrencyViewSet(CrmListModelMixin):
    permission_classes = (AdminPermissions,)
    queryset = Currency.objects.active().order_by('name')
    serializer_class = CurrencySerializer

    filter_backends = (CustomSearchFilter, CustomOrderingFilter)
    search_fields = ('^name',)
    ordering_fields = ('name',)
