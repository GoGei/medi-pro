from django.urls import include, path, re_path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)
from rest_framework.permissions import AllowAny


def make_schema_view(
        urls,
        v: str = 'v1',
        prefix: str = '',
        name: str = 'schema'
):
    class CustomSpectacularAPIView(SpectacularAPIView):
        permission_classes = [AllowAny]
        patterns = [re_path(f'{v}/{prefix}', include(urls))]

    return path(f'{prefix}schema/', CustomSpectacularAPIView.as_view(), name=name)


def get_patterns(
        urls,
        v: str = 'v1',
        schema_v: str = 'v1',
        namespace: str = 'public',
        prefix: str = ''
):
    return [
        make_schema_view(urls, v=schema_v, prefix=prefix, name=f'{namespace}-schema'),
        path(f'{prefix}swagger/', SpectacularSwaggerView.as_view(url_name=f'api-{v}:{namespace}-schema'),
             name=f'swagger-{namespace}'),
        path(f'{prefix}redoc/', SpectacularRedocView.as_view(url_name=f'api-{v}:{namespace}-schema'),
             name=f'redoc-{namespace}'),
    ]
