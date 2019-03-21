# -*- coding: utf-8 -*-



from cms.app_base import CMSApp
from cms.apphook_pool import apphook_pool
from django.urls import path

from .views import PositionDetailView, CourseDetailView


@apphook_pool.register
class PositionsApphook(CMSApp):
    name = "Positions"
    permissions = False

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path('<slug:slug>/', PositionDetailView.as_view(), name="position-detail")
        ]


@apphook_pool.register
class CourseApp(CMSApp):
    name = "Course"
    permissions = True

    def get_urls(self, page=None, language=None, **kwargs):
        return [
            path('<slug:slug>/', CourseDetailView.as_view(), name="course-detail")
        ]
