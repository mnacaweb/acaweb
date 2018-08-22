# coding: utf-8

from __future__ import unicode_literals

from adminsortable.admin import SortableAdmin
from django.contrib import admin
from filer.admin import FileAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from models import FilerVideo, Review, TeamMember, Link, Contact


@admin.register(FilerVideo)
class FilerVideoAdmin(FileAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(TabbedTranslationAdmin):
    pass


@admin.register(TeamMember)
class TeamMemberAdmin(TabbedTranslationAdmin):
    pass


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {
            'fields': (
                'text',
                ('external_link', 'internal_link'),
            )
        }),
        ('Link settings', {
            'classes': ('collapse',),
            'fields': (
                ('mailto', 'phone'),
                'target',
            )
        })
    ]


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    readonly_fields = ["name", "email", "created"]
    search_fields = ("text", "email", "name")
    list_filter = ("language", "purpose")
    list_display = ("name", "email", "purpose", "language")
    date_hierarchy = 'created'
    fieldsets = [
        (None, {"fields": (("name", "email"), "text")}),
        ("Meta", {"fields": (("language", "created"),)})
    ]

    def has_add_permission(self, request):
        return False
