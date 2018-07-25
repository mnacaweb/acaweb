# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.conf.urls import url

from .views import PositionDetailView, CourseDetailView


@apphook_pool.register
class PositionsApphook(CMSApp):
    name = "Positions"
    permissions = False

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            url(r'^(?P<slug>[\w-]+)/$', PositionDetailView.as_view(), name="position-detail")
        ]


@apphook_pool.register
class CourseApp(CMSApp):
    name = "Course"
    permissions = True

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            url(r'^(?P<slug>[\w-]+)/$', CourseDetailView.as_view(), name="course-detail")
        ]
