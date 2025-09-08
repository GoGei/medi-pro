from django.conf import settings
from rest_framework.routers import DefaultRouter
from .Country.views import CountryViewSet
from .Currency.views import CurrencyViewSet
from .Timezones.views import TimezoneHandbookViewSet

v1_router = DefaultRouter()
v1_router.register('countries', CountryViewSet, basename='countries')
v1_router.register('currencies', CurrencyViewSet, basename='currencies')
v1_router.register('timezones', TimezoneHandbookViewSet, basename='timezones')
urlpatterns = v1_router.urls

if settings.API_DOCUMENTATION:
    from Api.documentation.patterns import get_patterns

    urlpatterns += get_patterns(urlpatterns, v='v1', schema_v='api/v1', namespace='admin-v1', prefix='')
