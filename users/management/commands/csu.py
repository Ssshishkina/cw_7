from django.conf import settings
from django.core.management import BaseCommand
from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin_admin@sky.pro',
            first_name='Admin',
            last_name='Adminov',
            telegram_id=settings.TELEGRAM_USER_ID,
            is_superuser=True,
            is_staff=True,
            is_active=True
        )
        user.set_password('vfif')
        user.save()
