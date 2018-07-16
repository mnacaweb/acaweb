# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url

from .api import ReviewApi, TeamGridApi

urlpatterns = [
    url(r'^reviews/$', ReviewApi.as_view(), name="reviews"),
    url(r'^reviews/(?P<id>[0-9]+)/$', ReviewApi.as_view(), name="reviews"),

    url(r'^team_grid/(?P<id>[0-9]+)/$', TeamGridApi.as_view(), name="team-grid"),
]