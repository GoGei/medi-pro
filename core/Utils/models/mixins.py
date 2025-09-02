import string
import time
from uuid import uuid4

from django.conf import settings
from django.db import models
from django.db.models import Q
from django.utils import timezone
from hashids import Hashids


class UUIDMixin(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)

    class Meta:
        abstract = True


class IsActiveQuerySet(models.QuerySet):
    def active(self):
        return self.filter(archived_stamp__isnull=True)

    def not_active(self):
        return self.filter(archived_stamp__isnull=False)

    def archive(self, user=None):
        self.update(archived_by=user, archived_stamp=timezone.now())


class IsActiveMixin(models.Model):
    created_stamp = models.DateTimeField(auto_now_add=True)
    updated_stamp = models.DateTimeField(null=True)
    archived_stamp = models.DateTimeField(null=True)

    created_by = models.ForeignKey('User.User', on_delete=models.PROTECT, null=True, related_name='+')
    updated_by = models.ForeignKey('User.User', on_delete=models.PROTECT, null=True, related_name='+')
    archived_by = models.ForeignKey('User.User', on_delete=models.PROTECT, null=True, related_name='+')

    objects = IsActiveQuerySet.as_manager()

    class Meta:
        abstract = True
        indexes = [
            models.Index(
                name='idx_active_only',
                fields=['archived_stamp'],
                condition=Q(archived_stamp__isnull=True),
            ),
            models.Index(
                name='idx_archived_only',
                fields=['archived_stamp'],
                condition=Q(archived_stamp__isnull=False),
            ),
        ]

    @property
    def is_active(self) -> bool:
        return self.archived_stamp is None

    def modify(self, user, commit=True):
        self.updated_by = user
        self.updated_stamp = timezone.now()
        if commit:
            self.save(update_fields=['updated_by', 'updated_stamp'])
        return self

    def archive(self, user=None, commit=True):
        self.archived_by = user
        self.archived_stamp = timezone.now()
        if commit:
            self.save(update_fields=['archived_by', 'archived_stamp'])
        return self

    def restore(self, user=None, commit=True):
        self.archived_by = None
        self.archived_stamp = None
        if commit:
            self.save(update_fields=['archived_by', 'archived_stamp'])
        self.modify(user=user, commit=commit)
        return self


class HashIDMixin(models.Model):
    HASHIDS_FIELDS: tuple[str, ...] = ('id',)
    HASHIDS_SALT: str = getattr(settings, 'HASHIDS_SALT') or settings.SECRET_KEY
    HASHIDS_MIN_LENGTH: int = getattr(settings, 'HASHIDS_MIN_LENGTH') or 8
    HASHIDS_ALPHABET: str = getattr(settings, 'HASHIDS_ALPHABET') or string.ascii_letters + string.digits

    class Meta:
        abstract = True

    @classmethod
    def _hashids(cls) -> Hashids:
        return Hashids(salt=cls.HASHIDS_SALT, min_length=cls.HASHIDS_MIN_LENGTH, alphabet=cls.HASHIDS_ALPHABET)

    @classmethod
    def encode(cls, *values: int) -> str:
        return cls._hashids().encode(*values)

    @classmethod
    def decode(cls, hashid: str) -> tuple[int, ...]:
        return tuple(cls._hashids().decode(hashid))

    @classmethod
    def get_queryset(cls):
        return cls.objects.all()

    def hashid(self, *args) -> str:
        values = [getattr(self, field) for field in self.HASHIDS_FIELDS]

        if not args:
            args = (int(time.time()) * 1_000_000,)  # add timestamp
        if args:
            values.append(*args)
        return self.encode(*values)

    @classmethod
    def get_by_hashid(cls, hashid: str):
        vals = cls.decode(hashid)
        if not vals:
            return None
        return cls.get_queryset().get(pk=vals[0])
