# -*- coding: utf-8 -*-


import base64
import json
import re

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()


@register.filter(name="json")
def json_filter(value):
    return json.dumps(value)


@register.filter(name="email_link")
def email_link(value):
    if value:
        mail = value.split("@")
        return "aca{}mar@{}".format(
            base64.b64encode(mail[0].encode()).decode(), mail[1]
        )
    return value


@register.filter(name="money")
@stringfilter
def money(value):
    new = re.sub("^(-?\d+)(\d{3})", "\g<1> \g<2>", value)
    if value == new:
        return "{} Kč".format(value)
    else:
        return money(new)
