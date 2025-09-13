import uuid
from django.core.management import call_command

from celery import Task
from celeryapp.celery import app
from core.Loggers.models import HandbookUpdateLog
from .redis import (
    BaseRedis,
    ExtractAllergyCauseRedis,
    ExtractAllergyTypesRedis,
    ExtractAllergyReactionRedis,
    LoadIcd10Redis,
)


class SingleInstanceTask(Task):
    abstract = True
    redis_cls: BaseRedis = None

    def __init__(self, *args, redis_cls=None, **kwargs):
        super().__init__(*args, **kwargs)
        if redis_cls:
            self.redis_cls = redis_cls

    def apply_async(self, args=None, kwargs=None, **options):
        redis_cls = getattr(self, 'redis_cls', None)
        if not redis_cls:
            raise RuntimeError(f'{self.name} must define redis_cls')

        redis = redis_cls()
        if redis.exists():
            raise ValueError(f'Task {self.name} already scheduled under ID: {redis.get()}')

        options.setdefault('task_id', str(uuid.uuid4()))
        redis.set(options.get('task_id'))
        return super().apply_async(args=args, kwargs=kwargs, **options)

    def on_success(self, retval, task_id, args, kwargs):
        self.redis_cls().delete()
        return super().on_success(retval, task_id, args, kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        self.redis_cls().delete()
        return super().on_failure(exc, task_id, args, kwargs, einfo)

    def on_retry(self, exc, task_id, args, kwargs, einfo):
        self.redis_cls().delete()
        return super().on_retry(exc, task_id, args, kwargs, einfo)


@app.task(ignore_result=True, bind=True, base=SingleInstanceTask, redis_cls=ExtractAllergyCauseRedis)
def extract_allergy_cause(self, user_id: int = None):
    call_command('extract_allergy_cause')
    HandbookUpdateLog.objects.create(
        user_id=user_id,
        handbook=HandbookUpdateLog.HandbookChoices.ALLERGY_CAUSE,
    )
    return True


@app.task(ignore_result=True, bind=True, base=SingleInstanceTask, redis_cls=ExtractAllergyTypesRedis)
def extract_allergy_types(self, user_id: int = None):
    call_command('extract_allergy_types')
    HandbookUpdateLog.objects.create(
        user_id=user_id,
        handbook=HandbookUpdateLog.HandbookChoices.ALLERGY_TYPE,
    )
    return True


@app.task(ignore_result=True, bind=True, base=SingleInstanceTask, redis_cls=ExtractAllergyReactionRedis)
def extract_allergy_reaction(self, user_id: int = None):
    call_command('extract_allergy_reaction')
    HandbookUpdateLog.objects.create(
        user_id=user_id,
        handbook=HandbookUpdateLog.HandbookChoices.ALLERGY_REACTION,
    )
    return True


@app.task(ignore_result=True, bind=True, base=SingleInstanceTask, redis_cls=LoadIcd10Redis)
def load_icd10(self, user_id: int = None):
    call_command('load_icd10')
    HandbookUpdateLog.objects.create(
        user_id=user_id,
        handbook=HandbookUpdateLog.HandbookChoices.ICD_10,
    )
    return True
