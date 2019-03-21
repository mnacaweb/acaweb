# -*- coding: utf-8 -*-



from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.utils.functional import SimpleLazyObject


def project_settings(request):
    return {'settings': settings}


def site(request):
    return {
        'site': SimpleLazyObject(lambda: get_current_site(request)),
    }
