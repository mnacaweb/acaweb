# -*- coding: utf-8 -*-


import os

from django.conf import settings
from django.contrib.staticfiles.finders import AppDirectoriesFinder
from django.core.files.storage import FileSystemStorage


class GruntStaticStorage(FileSystemStorage):
    def __init__(self, location, *args, **kwargs):
        loc = os.path.join(
            settings.BASE_DIR, settings.INSTALLED_APPS[-1], settings.STATIC_GRUNT_DIR
        )
        super(GruntStaticStorage, self).__init__(loc, *args, **kwargs)


class GruntDirectoriesFinder(AppDirectoriesFinder):
    storage_class = GruntStaticStorage
