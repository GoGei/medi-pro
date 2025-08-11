from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from core.Utils.models.mixins import HashIDMixin


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email and password.
        """
        if not email:
            raise ValueError(_("The Email must be set"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff"):
            raise ValueError(_("User must have is_staff=False."))
        if extra_fields.get("is_superuser"):
            raise ValueError(_("User must have is_superuser=False."))
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if not extra_fields.get("is_staff"):
            raise ValueError(_("User must have is_staff=True."))
        if not extra_fields.get("is_superuser"):
            raise ValueError(_("User must have is_superuser=True."))
        return self._create_user(email, password, **extra_fields)


class User(AbstractUser, HashIDMixin):
    username = None
    email = models.EmailField(unique=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(null=True)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=70, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.email:
            self.email = None
        super().save(*args, **kwargs)

    def __str__(self):
        return self.email
