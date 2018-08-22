# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.admin.placeholderadmin import PlaceholderAdminMixin
from django.contrib import admin
from modeltranslation.admin import TabbedTranslationAdmin, TranslationStackedInline
from safedelete.admin import SafeDeleteAdmin, highlight_deleted

from .models import Course, CourseTerm, CourseTermItem, CourseEnroll, PositionApply, Recruiter


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
    list_filter = ("courses",)
    readonly_fields = ["courses", "name", "phone", "cv", "created"]
    date_hierarchy = "created"
    fieldsets = [
        (None, {"fields": (("name", "phone"), "courses", "expectations", "cv", "created")})
    ]

    def has_add_permission(self, request):
        return False


@admin.register(PositionApply)
class PositionApplyAdmin(admin.ModelAdmin):
    list_display = ("position_name", "first_name", "last_name", "email", "phone")
    list_filter = ("position_name",)
    readonly_fields = ["position", "position_name", "position_user_name", "position_user_email", "created"]
    date_hierarchy = "created"
    fieldsets = [
        ("Position", {"fields": ["position_name", ("position_user_name", "position_user_email")]}),
        ("Application", {"fields": [("first_name", "last_name"), ("email", "phone"), ("linkedin",), "cv", "text"]})
    ]

    def has_add_permission(self, request):
        return False


@admin.register(Recruiter)
class RecruiterAdmin(admin.ModelAdmin):
    pass
