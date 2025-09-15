from default_settings import *  # noqa

SECRET_KEY = 'your-secret-key'
WS_SECRET = 'your-secret-key'
DEBUG = True

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
