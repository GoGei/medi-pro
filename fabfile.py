import os
from fabric import task
from django.conf import settings as dj_settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')


@task
def runserver(c):
    host = dj_settings.PARENT_HOST
    port = dj_settings.HOST_PORT
    c.run(f'./manage.py runserver {host}:{port}', pty=True)


@task
def recompilerequirements(c):
    c.run("rm -f pyproject.toml uv.lock")
    pyproject = """[project]
name = "medi-pro"
version = "0.1.0"
requires-python = ">=3.11"

dependencies = []
"""
    with open("pyproject.toml", "w") as f:
        f.write(pyproject)

    c.run("uv add -r requirements.txt --python 3.11 --active")
    c.run("uv lock --python 3.11")
    c.run("uv sync --frozen --active --python 3.11")


@task
def compilerequirements(c):
    c.run("uv add -r requirements.txt --python 3.11 --active")
    c.run("uv lock --python 3.11")


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
