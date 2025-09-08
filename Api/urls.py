from django.conf import settings
from django.conf.urls import include
from django.urls import path

from Api.v1.urls import urlpatterns as v1_urls

urlpatterns = [
    path(r'', include('rest_framework.urls', namespace='rest_framework')),
    path('v1/', include((v1_urls, 'api'), namespace='api-v1')),
]

if not settings.TEST:
    # somehow cause "RecursionError: maximum recursion depth exceeded in __instancecheck__"
    urlpatterns += [
        path(r'', include('urls')),
    ]
