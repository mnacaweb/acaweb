# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import base64
import json

from django import template

register = template.Library()


@register.filter(name="json")
def json_filter(value):
    return json.dumps(value)


@register.filter(name="email_link")
def email_link(value):
    mail = value.split("@")
    return "aca{}mar@{}".format(base64.b64encode(mail[0]), mail[1])