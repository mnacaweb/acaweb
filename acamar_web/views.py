# encoding: utf-8

from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic import DetailView

from acamar_api.models import Position


def handler404(request):
    response = render(request, '404.html')
    response.status_code = 404
    return response


class PositionDetailView(DetailView):
    model = Position
    template_name = "apps/position_detail.html"

    def get_context_data(self, **kwargs):
        context = super(PositionDetailView, self).get_context_data(**kwargs)
        context['meta'] = self.get_object().as_meta(self.request)
        return context
