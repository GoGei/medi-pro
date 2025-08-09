import os
from fabric import task
from django.conf import settings as dj_settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "configs.settings")


@task
def runserver(c):
    host = dj_settings.SITE_HOST
    port = dj_settings.SITE_PORT
    c.run(f"./manage.py runserver {host}:{port}", pty=True)

@task
def compilerequirements(c):
    c.run("uv pip compile requirements.txt -o requirements.lock")