# -*- coding: utf-8 -*-


from modeltranslation.translator import TranslationOptions, register

from .models import (
    PositionCategory,
    PositionPact,
    PositionTechnology,
    Position,
    Course,
    CourseTermItem,
)


@register(PositionCategory)
class PositionCategoryTranslationOptions(TranslationOptions):
    fields = ["name"]


@register(PositionPact)
class PositionPactTranslationOptions(TranslationOptions):
    fields = ["name"]


@register(PositionTechnology)
class PositionTechnologyTranslationOptions(TranslationOptions):
    fields = ["name"]


@register(Course)
class CourseTranslationOptions(TranslationOptions):
    fields = [
        "title",
        "slug",
        "short_description",
        "place",
        "duration",
        "price",
        "meta_title",
        "meta_description",
        "meta_keywords",
    ]


@register(CourseTermItem)
class CourseTermItemTranslationOptions(TranslationOptions):
    fields = ["address", "description"]
