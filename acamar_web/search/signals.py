# -*- coding: utf-8 -*-


from django.db import models
from haystack.signals import BaseSignalProcessor

from acamar_api.models import Position


class PositionRealtimeSignalProcessor(BaseSignalProcessor):
    def setup(self):
        models.signals.post_save.connect(self.handle_save, sender=Position)
        models.signals.post_delete.connect(self.handle_delete, sender=Position)

    def teardown(self):
        models.signals.post_save.disconnect(self.handle_save, sender=Position)
        models.signals.post_delete.disconnect(self.handle_delete, sender=Position)
