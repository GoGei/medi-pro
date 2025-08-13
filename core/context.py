from django.conf import settings


def app_context(request):
    return {
        'APP_NAME': settings.APP_NAME,
        'SHORT_APP_NAME': settings.SHORT_APP_NAME,
    }
