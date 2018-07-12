# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from filer.fields.file import FilerFileField

from .models import FilerVideo


class FilerVideoField(FilerFileField):
    default_model_class = FilerVideo
