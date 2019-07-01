# encoding: utf-8

from urllib.parse import urlparse

from django.contrib.sites.models import Site
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.utils.translation import get_language
from django.views import View
from django.views.generic import DetailView, TemplateView

from acamar_api.models import Position, Course


class Error404View(View):
    def get(self, *args, **kwargs):
        url = self.request.META.get("HTTP_REFERER", "")
        link = "/"
        if url and urlparse(Site.objects.get_current(self.request).domain).netloc in url:
            link = url

        html = render(self.request, '404.html', {'link': link})
        return HttpResponseNotFound(html)

#
class PositionDetailView(DetailView):
    model = Position
    template_name = "apps/position_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PositionDetailView, self).get_context_data(**kwargs)
        context["meta"] = self.get_object().as_meta(self.request)
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
        context["meta"] = self.get_object().as_meta(self.request)
        return context
