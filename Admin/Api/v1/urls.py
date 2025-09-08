from django.conf import settings
from rest_framework.routers import DefaultRouter
from .Currency.views import CurrencyViewSet

v1_router = DefaultRouter()
v1_router.register('currency', CurrencyViewSet, basename='currency')
urlpatterns = v1_router.urls

if settings.API_DOCUMENTATION:
    from Api.documentation.patterns import get_patterns

    urlpatterns += get_patterns(urlpatterns, v='v1', schema_v='api/v1', namespace='admin-v1', prefix='')
