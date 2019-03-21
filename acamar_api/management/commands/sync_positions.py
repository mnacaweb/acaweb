# -*- coding: utf-8 -*-



from django.core.management.base import BaseCommand

from acamar_api.acamar_api import AcamarPositionManager


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        AcamarPositionManager.sync()
