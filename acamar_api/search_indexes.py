# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils import translation
from django.utils.html_parser import HTMLParser
from haystack import indexes

from .models import Position
from acamar_web.haystack.utils import get_language_from_alias


class PositionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    autocomplete = indexes.EdgeNgramField(model_attr="title1")

    def __init__(self):
        super(PositionIndex, self).__init__()
        self.language = None

    def get_model(self):
        return Position

    def prepare(self, obj):
        with translation.override(self.language):
            data = super(PositionIndex, self).prepare(obj)
            return data

    def prepare_text(self, obj):
        parser = HTMLParser()
        return parser.unescape(self.prepared_data["text"])

    def index_queryset(self, using=None):
        language = get_language_from_alias(using)
        self.language = language
        return self.get_model().objects_default.filter(**{"lang_{}".format(language): True})
