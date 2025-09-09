from django.core.management import call_command

from celeryapp.celery import app


@app.task(ignore_result=True)
def extract_allergy_cause(user_id: int = None):
    try:
        call_command('extract_allergy_cause', user_id=user_id)
        return True
    except Exception as e:
        print(f'task extract_allergy_cause failed with exception: {e}')
        return False


@app.task(ignore_result=True)
def extract_allergy_types(user_id: int = None):
    try:
        call_command('extract_allergy_types', user_id=user_id)
        return True
    except Exception as e:
        print(f'task extract_allergy_types failed with exception: {e}')
        return False


@app.task(ignore_result=True)
def extract_allergy_reaction(user_id: int = None):
    try:
        call_command('extract_allergy_reaction', user_id=user_id)
        return True
    except Exception as e:
        print(f'task extract_allergy_reaction failed with exception: {e}')
        return False


@app.task(ignore_result=True)
def load_icd10(user_id: int = None):
    try:
        call_command('load_icd10', user_id=user_id)
        return True
    except Exception as e:
        print(f'task load_icd10 failed with exception: {e}')
        return False
