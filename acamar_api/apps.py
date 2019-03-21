# -*- coding: utf-8 -*-


from django.apps import AppConfig


class AcamarApiConfig(AppConfig):
    name = "acamar_api"
    verbose_name = "Acamar api"

    def ready(self):
        from . import signals

        signals._()  # magic
