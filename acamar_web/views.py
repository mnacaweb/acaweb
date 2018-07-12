# encoding: utf-8

from __future__ import unicode_literals

from django.utils import timezone
from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseBadRequest
from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from django.conf import settings
