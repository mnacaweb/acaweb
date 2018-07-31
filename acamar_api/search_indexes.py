# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.utils import translation
from django.utils.html_parser import HTMLParser
from haystack import indexes

from .models import Position
from acamar_web.haystack.utils import get_language_from_alias


class PositionIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    autocomplete = indexes.EdgeNgramField(model_attr="name")
    category_id = indexes.IntegerField(model_attr="category_id", indexed=False)
    pacts_json = indexes.CharField(model_attr="pacts_json", indexed=False)
    url = indexes.CharField(model_attr="url", indexed=False)
    name = indexes.CharField(model_attr="name", indexed=False)
    technologies_text = indexes.CharField(model_attr="technologies_text", indexed=False)
    pacts_text = indexes.CharField(model_attr="pacts_text", indexed=False)
    place = indexes.CharField(model_attr="place", indexed=False)
    user_image_url = indexes.CharField(model_attr="user_image_url", indexed=False)
    user_first_name = indexes.CharField(model_attr="user_first_name", indexed=False)
    user_second_name = indexes.CharField(model_attr="user_second_name", indexed=False)
    user_position = indexes.CharField(model_attr="user_position", indexed=False)
    user_email = indexes.CharField(model_attr="user_email", indexed=False)

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
