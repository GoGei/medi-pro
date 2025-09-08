from django.conf.urls import include
from django.urls import path

from Admin.Api.v1.urls import urlpatterns as v1_urls

handler404 = "Api.errors.views.error404"
handler500 = "Api.errors.views.error500"
handler403 = "Api.errors.views.error403"

urlpatterns = [
    path('v1/', include((v1_urls, 'api'), namespace='api-v1')),
]
