# coding: utf-8

from __future__ import unicode_literals

from adminsortable.admin import SortableAdmin
from django.contrib import admin
from filer.admin import FileAdmin

from models import FilerVideo, Review, TeamMember


@admin.register(FilerVideo)
class FilerVideoAdmin(FileAdmin):
    pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass


@admin.register(TeamMember)
class TeamMemberAdmin(SortableAdmin):
    pass