# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from modeltranslation.translator import TranslationOptions, register

from .models import PositionCategory, PositionPact, PositionTechnology, Position


@register(PositionCategory)
class PositionCategoryTranslationOptions(TranslationOptions):
    fields = ["name"]


@register(PositionPact)
class PositionPactTranslationOptions(TranslationOptions):
    fields = ["name"]


@register(PositionTechnology)
class PositionTechnologyTranslationOptions(TranslationOptions):
    fields = ["name"]


@register(Position)
class PositionTranslationOPtions(TranslationOptions):
    fields = ["lang", "place", "start", "name", "introduction", "title1", "title2", "title3", "title4", "title5", "title6",
              "text1", "text2", "text3", "text4", "text5", "text6", "user_position"]
