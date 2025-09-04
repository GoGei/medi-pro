from django.core.management import call_command

from celeryapp.celery import app


@app.task(ignore_result=True)
def extract_allergy_cause():
    try:
        call_command('extract_allergy_cause')
        return True
    except Exception as e:
        print(f'task extract_allergy_cause failed with exception: {e}')
        return False


@app.task(ignore_result=True)
def extract_allergy_types():
    try:
        call_command('extract_allergy_types')
        return True
    except Exception as e:
        print(f'task extract_allergy_types failed with exception: {e}')
        return False


@app.task(ignore_result=True)
def extract_allergy_reaction():
    try:
        call_command('extract_allergy_reaction')
        return True
    except Exception as e:
        print(f'task extract_allergy_reaction failed with exception: {e}')
        return False


@app.task(ignore_result=True)
def load_icd10():
    try:
        call_command('load_icd10')
        return True
    except Exception as e:
        print(f'task load_icd10 failed with exception: {e}')
        return False
