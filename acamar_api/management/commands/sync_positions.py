from django.core.management.base import BaseCommand

from acamar_api.manager import AcamarPositionManager


class Command(BaseCommand):
    help = "My shiny new management command."

    def handle(self, *args, **options):
        AcamarPositionManager.sync_categories()
        AcamarPositionManager.sync_technologies()
        AcamarPositionManager.sync_pacts()
        AcamarPositionManager.sync_positions()

