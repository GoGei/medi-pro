from django.core.management import call_command

from celeryapp.celery import app
from core.Loggers.models import HandbookUpdateLog


@app.task(ignore_result=True)
def extract_allergy_cause(user_id: int = None):
    try:
        call_command('extract_allergy_cause')
        HandbookUpdateLog.objects.create(user_id=user_id, handbook=HandbookUpdateLog.HandbookChoices.ALLERGY_CAUSE)
        return True
    except Exception as e:
        print(f'task extract_allergy_cause failed with exception: {e}')
        return False


@app.task(ignore_result=True)
def extract_allergy_types(user_id: int = None):
    try:
        call_command('extract_allergy_types')
        HandbookUpdateLog.objects.create(user_id=user_id, handbook=HandbookUpdateLog.HandbookChoices.ALLERGY_TYPE)
        return True
    except Exception as e:
        print(f'task extract_allergy_types failed with exception: {e}')
        return False


@app.task(ignore_result=True)
def extract_allergy_reaction(user_id: int = None):
    try:
        call_command('extract_allergy_reaction')
        HandbookUpdateLog.objects.create(user_id=user_id, handbook=HandbookUpdateLog.HandbookChoices.ALLERGY_REACTION)
        return True
    except Exception as e:
        print(f'task extract_allergy_reaction failed with exception: {e}')
        return False


@app.task(ignore_result=True)
def load_icd10(user_id: int = None):
    try:
        call_command('load_icd10')
        HandbookUpdateLog.objects.create(user_id=user_id, handbook=HandbookUpdateLog.HandbookChoices.ICD_10)
        return True
    except Exception as e:
        print(f'task load_icd10 failed with exception: {e}')
        return False
