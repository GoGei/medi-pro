from default_settings import *  # noqa

SECRET_KEY = 'your-secret-key'
DEBUG = True

WS_SECRET = 'your-secret-key'
WS_SCHEME = 'ws'
WS_LOCATION = 'localhost:8081'
WS_BASE = f'{WS_SCHEME}://{WS_LOCATION}'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "medipro",
        "USER": "medipro_user",
        "PASSWORD": "medipro_password",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
