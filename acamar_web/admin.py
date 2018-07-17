# coding: utf-8

from __future__ import unicode_literals

from adminsortable.admin import SortableAdmin
from django.contrib import admin
from filer.admin import FileAdmin
from modeltranslation.admin import TabbedTranslationAdmin

from models import FilerVideo, Review, TeamMember


@admin.register(FilerVideo)
class FilerVideoAdmin(FileAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(TabbedTranslationAdmin):
    pass


@admin.register(TeamMember)
class TeamMemberAdmin(SortableAdmin, TabbedTranslationAdmin):
    pass
