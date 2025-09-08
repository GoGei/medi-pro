from django.conf import settings
from django.conf.urls import include
from django.urls import path

from .PublicPart.urls import urlpatterns as public_part_urls

urlpatterns = [
    path('', include((public_part_urls, 'public'), namespace='public')),
    # path('clinic/', include((clinic_part_urls, 'clinic'), namespace='clinic')),
]

if settings.API_DOCUMENTATION:
    from Api.documentation.patterns import get_patterns

    urlpatterns += get_patterns(public_part_urls, v='v1', namespace='public', prefix='')
    # urlpatterns += get_patterns(clinic_part_urls, v='v1', namespace='clinic', prefix='clinic/')
