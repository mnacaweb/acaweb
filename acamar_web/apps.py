# coding: utf-8

from django.apps import AppConfig


class AcamarAppConfig(AppConfig):
    name = "acamar_web"
    verbose_name = "Acamar web"

    def ready(self):
        from . import signals

        signals._()  # magic
