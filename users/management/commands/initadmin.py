import os

from django.core.management.base import BaseCommand

from users.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):
        if not User.objects.filter(username="admin").exists():
            username = os.getenv('DJANGO_SUPERUSER_USERNAME')
            email = os.getenv('DJANGO_SUPERUSER_EMAIL')
            password = os.getenv('DJANGO_SUPERUSER_PASSWORD')
            print('Creating account for %s (%s)' % (username, email))
            admin = User.objects.create_superuser(email=email, username=username, password=password)
            admin.is_active = True
            admin.is_admin = True
            admin.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')
