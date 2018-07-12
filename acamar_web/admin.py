# coding: utf-8

from __future__ import unicode_literals

from django.contrib import admin
from filer.admin import FileAdmin

from models import FilerVideo


@admin.register(FilerVideo)
class FilerVideoAdmin(FileAdmin):
    pass
