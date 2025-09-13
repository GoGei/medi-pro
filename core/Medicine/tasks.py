from django.core.management import call_command

from celeryapp.celery import app
from core.Loggers.models import HandbookUpdateLog
from .redis import (
    ExtractAllergyCauseRedis,
    ExtractAllergyTypesRedis,
    ExtractAllergyReactionRedis,
    LoadIcd10Redis,
)


@app.task(ignore_result=True, bind=True)
def extract_allergy_cause(self, user_id: int = None):
    redis_cls = ExtractAllergyCauseRedis()
    if redis_cls.exists():
        task_id = redis_cls.get()
        print(f'Task extract_allergy_cause in progress under ID: {task_id}')
        return False

    try:
        redis_cls.set(self.request.id)
        call_command('extract_allergy_cause')
        HandbookUpdateLog.objects.create(user_id=user_id, handbook=HandbookUpdateLog.HandbookChoices.ALLERGY_CAUSE)
        return True
    except Exception as e:
        print(f'task extract_allergy_cause failed with exception: {e}')
        return False
    finally:
        redis_cls.delete()


@app.task(ignore_result=True, bind=True)
def extract_allergy_types(self, user_id: int = None):
    redis_cls = ExtractAllergyTypesRedis()
    if redis_cls.exists():
        task_id = redis_cls.get()
        print(f'Task extract_allergy_types in progress under ID: {task_id}')
        return False

    try:
        redis_cls.set(self.request.id)
        call_command('extract_allergy_types')
        HandbookUpdateLog.objects.create(user_id=user_id, handbook=HandbookUpdateLog.HandbookChoices.ALLERGY_TYPE)
        return True
    except Exception as e:
        print(f'task extract_allergy_types failed with exception: {e}')
        return False
    finally:
        redis_cls.delete()


@app.task(ignore_result=True, bind=True)
def extract_allergy_reaction(self, user_id: int = None):
    redis_cls = ExtractAllergyReactionRedis()
    if redis_cls.exists():
        task_id = redis_cls.get()
        print(f'Task extract_allergy_reaction in progress under ID: {task_id}')
        return False

    try:
        redis_cls.set(self.request.id)
        call_command('extract_allergy_reaction')
        HandbookUpdateLog.objects.create(user_id=user_id, handbook=HandbookUpdateLog.HandbookChoices.ALLERGY_REACTION)
        return True
    except Exception as e:
        print(f'task extract_allergy_reaction failed with exception: {e}')
        return False
    finally:
        redis_cls.delete()


@app.task(ignore_result=True, bind=True)
def load_icd10(self, user_id: int = None):
    redis_cls = LoadIcd10Redis()
    if redis_cls.exists():
        task_id = redis_cls.get()
        print(f'Task load_icd10 in progress under ID: {task_id}')
        return False

    try:
        redis_cls.set(self.request.id)
        call_command('load_icd10')
        HandbookUpdateLog.objects.create(user_id=user_id, handbook=HandbookUpdateLog.HandbookChoices.ICD_10)
        return True
    except Exception as e:
        print(f'task load_icd10 failed with exception: {e}')
        return False
    finally:
        redis_cls.delete()
