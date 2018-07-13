# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url

from .api import ReviewApi

urlpatterns = [
    url(r'^reviews/$', ReviewApi.as_view(), name="reviews"),
    url(r'^reviews/(?P<id>[0-9]+)/$', ReviewApi.as_view(), name="reviews"),
]