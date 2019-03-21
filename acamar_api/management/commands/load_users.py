# -*- coding: utf-8 -*-



import csv
import os

from cms.models import User
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        with open(os.path.join(settings.BASE_DIR, "backups/Acarta_Login.csv")) as f:
            reader = csv.reader(f, delimiter=b";")
            for row in reader:
                name = row[0].decode("utf-8").split(" ")
                user = User.objects.create_user(
                    first_name=name[0],
                    last_name=name[1],
                    password=row[1].decode("utf-8").strip(),
                    email=row[2].decode("utf-8").strip(),
                    username=row[2].decode("utf-8").strip()
                )
