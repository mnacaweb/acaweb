# encoding: utf-8

from __future__ import unicode_literals

from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseBadRequest
from django.template.context import RequestContext
from django.shortcuts import render_to_response, render
from django.core.urlresolvers import reverse
from django.conf import settings


def handler404(request):
    response = render(request, '404.html')
    response.status_code = 404
    return response