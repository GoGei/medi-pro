import os
from django.core.management.base import BaseCommand, CommandError
from core.User.models import User


class Command(BaseCommand):
    help = "Create a superuser"

    def handle(self, *args, **options):
        email = os.getenv("DJANGO_SUPERUSER_EMAIL")
        password = os.getenv("DJANGO_SUPERUSER_PASSWORD")
        if not email:
            raise CommandError("DJANGO_SUPERUSER_EMAIL must be set to execute this command")
        if not password:
            raise CommandError("DJANGO_SUPERUSER_PASSWORD must be set to execute this command")

        email = email.lower().strip()
        if User.objects.filter(email__iexact=email).exists():
            self.stdout.write(self.style.WARNING("Superuser already exists"))
            return
        try:
            User.objects.create_superuser(email=email, password=password)
            self.stdout.write(self.style.SUCCESS("Superuser created"))
        except Exception as e:
            raise CommandError(str(e))
