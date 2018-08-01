# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.admin.placeholderadmin import PlaceholderAdminMixin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from safedelete.admin import SafeDeleteAdmin, highlight_deleted

from .models import Course, CourseTerm, CourseTermItem, CourseEnroll


@admin.register(Course)
class CourseAdmin(PlaceholderAdminMixin, SafeDeleteAdmin, TabbedTranslationAdmin):
    list_display = (highlight_deleted,) + SafeDeleteAdmin.list_display
    prepopulated_fields = {'slug': ('title',)}
    fieldsets = [
        (None,
         {"fields": [("title", "slug"), ("place", "price", "duration"), "short_description"]}),
        ("Meta fields", {"fields": ["meta_title", "meta_description", "meta_keywords"], "classes": ["collapse"]})
    ]


class CourseTermItemInline(TranslationStackedInline):
    model = CourseTermItem
    min_num = 1
    extra = 1
    fieldsets = (
        (None, {"fields": (("date", "start_time", "end_time"), "address", "description")}),
    )


@admin.register(CourseTerm)
class CourseTermAdmin(SafeDeleteAdmin):
    inlines = [CourseTermItemInline]
    search_fields = ["course__title"]
    list_display = (highlight_deleted,) + SafeDeleteAdmin.list_display
    list_filter = SafeDeleteAdmin.list_filter + ("course__title",)
    save_as = True

    class Media:
        js = (
            'modeltranslation/js/force_jquery.js',
            'http://ajax.googleapis.com/ajax/libs/jqueryui/1.8.24/jquery-ui.min.js',
            'modeltranslation/js/tabbed_translation_fields.js',
        )
        css = {
            'screen': ('modeltranslation/css/tabbed_translation_fields.css',),
        }


@admin.register(CourseEnroll)
class CourseEnrollAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "course_list")
    readonly_fields = ["courses", "name", "phone", "cv", "created"]
    date_hierarchy = "created"
    fieldsets = [
        (None, {"fields": (("name", "phone"), "courses", "expectations", "cv", "created")})
    ]

    def has_add_permission(self, request):
        return False

    def course_list(self, obj):
        return ", ".join(Course.objects.filter(terms__in=obj.courses.all()).values_list("title", flat=True))
