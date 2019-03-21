# -*- coding: utf-8 -*-



from modeltranslation.translator import TranslationOptions, register

from acamar_web.models import Review, TeamMember, Link


@register(Review)
class ReviewTranslationOptions(TranslationOptions):
    fields = ["author", "text"]


@register(TeamMember)
class TeamMemberTranslationOptions(TranslationOptions):
    fields = ["name", "nickname", "text"]


@register(Link)
class LinkTranslationOptions(TranslationOptions):
    fields = ["text"]
