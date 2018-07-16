# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http.response import HttpResponseNotAllowed
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from .models import Review


class ReviewApi(View):
    def get(self, request, id=None):
        if id:
            object = get_object_or_404(Review, pk=id, show=True)
            return render(request, "plugins/review_panel/review.html", {"object": object})
        else:
            return HttpResponseNotAllowed([])
