# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from modeltranslation.translator import TranslationOptions, register

from .models import PositionCategory, PositionPact, PositionTechnology, Position, Course, CourseTermItem


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
class PositionTranslationOptions(TranslationOptions):
    fields = ["lang", "place", "start", "name", "slug", "introduction", "title1", "title2", "title3", "title4",
              "title5", "title6", "text1", "text2", "text3", "text4", "text5", "text6", "user_position"]


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = ["title", "slug", "short_description", "place", "duration", "price", "meta_title", "meta_description",
              "meta_keywords"]


@register(CourseTermItem)
class CourseTermItemTranslationOptions(TranslationOptions):
    fields = ["address", "description"]
