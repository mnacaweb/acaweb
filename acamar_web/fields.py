# -*- coding: utf-8 -*-


from filer.fields.file import FilerFileField

from .models import FilerVideo


class FilerVideoField(FilerFileField):
    default_model_class = FilerVideo
