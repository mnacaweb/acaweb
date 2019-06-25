# encoding: utf-8

from __future__ import unicode_literals

from urlparse import urlparse

from django.contrib.sites.models import Site
from django.shortcuts import render
from django.utils.translation import get_language
from django.views.generic import DetailView

from acamar_api.models import Position, Course


def handler404(request):
    url = request.META.get("HTTP_REFERER", "")
    link = "/"
    if url and urlparse(Site.objects.get_current(request).domain).netloc in url:
        link = url
    response = render(request, '404.html', {"link": link})
    response.status_code = 404
    return response


class PositionDetailView(DetailView):
    model = Position
    template_name = "apps/position_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PositionDetailView, self).get_context_data(**kwargs)
        context['meta'] = self.get_object().as_meta(self.request)

        return context

    def dictfetchall(cursor):
        "Return all rows from a cursor as a dict"
        columns = [col[0] for col in cursor.description]
        return [
            dict(zip(columns, row))
            for row in cursor.fetchall()
        ]

    def get_queryset(self):
        qs = super(PositionDetailView, self).get_queryset()
        language = get_language()
        qs = qs.filter(lang=language).exclude(slug="")
        return qs


class CourseDetailView(DetailView):
    model = Course
    template_name = "apps/course_detail.html"

    def get_context_data(self, **kwargs):
        context = super(CourseDetailView, self).get_context_data(**kwargs)
        context['meta'] = self.get_object().as_meta(self.request)
        return context
