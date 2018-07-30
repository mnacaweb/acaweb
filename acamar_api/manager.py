# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class PositionManager(models.Manager):
    def get_queryset(self):
        return super(PositionManager, self).get_queryset().filter(lang=True)
