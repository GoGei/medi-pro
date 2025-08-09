from default_settings import *  # noqa

SECRET_KEY = 'your-secret-key'
DEBUG = True

ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '.medi-pro', '.medi-pro.local']

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
