# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf import settings


def project_settings(request):
    return {'settings': settings}
