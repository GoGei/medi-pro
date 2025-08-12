import os
from fabric import task
from django.conf import settings as dj_settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')


@task
def runserver(c):
    host = dj_settings.SITE_HOST
    port = dj_settings.SITE_PORT
    c.run(f'./manage.py runserver {host}:{port}', pty=True)


@task
def compilerequirements(c):
    c.run('uv pip compile requirements.txt -o requirements.lock')


@task
def makemessages(c):
    c.run(f'./manage.py makemessages --all --no-location')


@task
def compilemessages(c):
    c.run(f'./manage.py compilemessages')


@task
def check(c):
    c.run('./manage.py check')
    c.run('flake8')


@task
def celeryrun(c):
    c.run('celery -A celeryapp worker --loglevel=info')


@task
def celerybeat(c):
    c.run('celery -A celeryapp beat --loglevel=info')
