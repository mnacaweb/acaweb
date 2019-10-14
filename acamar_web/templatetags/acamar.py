# -*- coding: utf-8 -*-


from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter

from cms.constants import PUBLISHER_STATE_PENDING
from cms.models import Page
from modeltranslation.utils import get_language

register = template.Library()


@register.filter(name="language_verbose")
@stringfilter
def language_verbose(value):
    return settings.LANGUAGES_VERBOSE.get(value, "")


@register.simple_tag
def is_page_published(page_id):
    page = Page.objects.get(pk=page_id)
    language = get_language()

    if page.is_published(language):
        return True

    page_languages = page.get_languages()

    if language in page_languages and page.get_publisher_state(language) == PUBLISHER_STATE_PENDING:
        return True
    return False
