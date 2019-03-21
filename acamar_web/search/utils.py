# -*- coding: utf-8 -*-



from django.conf import settings


def get_alias_from_language(language):
    return "default_{}".format(language)


def get_language_from_alias(alias):
    lang = alias.split("_")
    if len(lang) == 2:
        return lang[1]
    return settings.LANGUAGE_CODE
