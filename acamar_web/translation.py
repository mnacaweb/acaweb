# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from modeltranslation.translator import TranslationOptions, register

from acamar_web.models import Review, TeamMember, Link


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ["author", "text"]


@register(TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = ["nickname", "text"]


@register(Link)
class LinkTranslationOptions(TranslationOptions):
    fields = ["text"]
