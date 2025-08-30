from django.core.management import call_command

from celeryapp.celery import app


@app.task(ignore_result=True)
def extract_allergy_cause():
    try:
        call_command('extract_allergy_cause')
        return True
    except Exception:
        return False
