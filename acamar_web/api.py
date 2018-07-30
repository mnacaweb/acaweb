# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.http.response import HttpResponseNotAllowed, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import View

from acamar_api.forms import PositionSearchForm, CourseEnrollForm
from acamar_api.models import Position
from .models import Review, TeamGrid, PositionSearch


class ReviewApi(View):
    def get(self, request, id=None):
        if id:
            object = get_object_or_404(Review, pk=id, show=True)
            return render(request, "plugins/review_panel/review.html", {"object": object})
        else:
            return HttpResponseNotAllowed([])


class TeamGridApi(View):
    def get(self, request, id):
        instance = get_object_or_404(TeamGrid, pk=id)
        return render(request, "plugins/team_grid/team_grid_ajax.html", {"instance": instance})


class PositionSearchApi(View):
    def get(self, request, id):
        instance = get_object_or_404(PositionSearch, pk=id)
        form = PositionSearchForm(request.GET, load_all=True)
        if form.is_valid():
            sqs = form.search()
            return render(request, "plugins/position_search/results.html", {
                "instance": instance,
                "objects": sqs,
                "suggestion": form.get_suggestion(),
                "limit": instance.limit,
                "more": (sqs.count() > instance.limit) if instance.limit else False
            })

        return


class PositionSearchAutocompleteApi(View):
    def get(self, request):
        sqs = Position.autocomplete(request.GET.get("q", "")).load_all()[:5]

        return render(request, "plugins/position_search/autocomplete.html", {"objects": sqs})


class CourseEnrollApi(View):
    def post(self, request):
        form = CourseEnrollForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True, "redirrect": ""})

        return JsonResponse({"success": False, "data": form.errors})
