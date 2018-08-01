# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.apps import AppConfig


class AcamarApiConfig(AppConfig):
    name = 'acamar_api'
    verbose_name = 'Acamar api'

    def ready(self):
        from . import signals
        signals._()  # magic
