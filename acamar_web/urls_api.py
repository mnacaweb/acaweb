# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.conf.urls import url

from .api import ReviewApi, TeamGridApi, PositionSearchApi, PositionSearchAutocompleteApi, CourseEnrollApi, login_api, \
    ContactApi

urlpatterns = [
    url(r'^reviews/$', ReviewApi.as_view(), name="reviews"),
    url(r'^reviews/(?P<id>[0-9]+)/$', ReviewApi.as_view(), name="reviews"),

    url(r'^team_grid/(?P<id>[0-9]+)/$', TeamGridApi.as_view(), name="team-grid"),

    url(r'^position_search/$', PositionSearchAutocompleteApi.as_view(), name="position-search-autocomplete"),
    url(r'^position_search/(?P<id>[0-9]+)/$', PositionSearchApi.as_view(), name="position-search"),

    url(r'^course_enroll/$', CourseEnrollApi.as_view(), name="course-enroll"),

    url(r'^login/$', login_api, name="login"),

    url(r'^contact/$', ContactApi.as_view(), name="contact")
]
