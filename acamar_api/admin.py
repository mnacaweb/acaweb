# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.admin.placeholderadmin import PlaceholderAdminMixin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline

from acamar_api.models import Course, CourseTerm, CourseTermItem


@admin.register(Course)
class CourseAdmin(PlaceholderAdminMixin, TabbedTranslationAdmin):
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = [
        (None, {"fields": [("title", "slug"), ("place", "price", "duration"), "short_description"]}),
        ("Additional fields", {"fields": ["meta_keywords"], "classes": ["collapse"]})
    ]


class CourseTermItemInline(TranslationStackedInline):
    model = CourseTermItem
    min_num = 1
    extra = 1
    fieldsets = (
        (None, {"fields": (("date", "start_time", "end_time"), "address", "description")}),
    )


@admin.register(CourseTerm)
class CourseTermAdmin(admin.ModelAdmin):
    inlines = [CourseTermItemInline]
    search_fields = ["course__title"]
    list_filter = ["course__title"]

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }
