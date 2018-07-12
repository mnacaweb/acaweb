# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import template
from django.conf import settings
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="language_verbose")
@stringfilter
def language_verbose(value):
    return settings.LANGUAGES_VERBOSE.get(value, "")
