import os

from celery import Celery

# from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')

app = Celery('medipro')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


# app.conf.beat_schedule = {
#     'task-slug': {
#         'task': 'path.to.task',
#         'schedule': crontab(minute='*/1'),
#     },
# }


@app.task(bind=True, ignore_result=True)
def debug_task(self, *args, **kwargs):
    print(f'Request: {self.request!r}, args: {args}, kwargs: {kwargs}')
