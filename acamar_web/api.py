# -*- coding: utf-8 -*-


from cms.models import Page
from django.conf import settings
from django.contrib.auth import REDIRECT_FIELD_NAME, login
from django.contrib.auth.forms import AuthenticationForm
from django.http.response import (
    HttpResponseNotAllowed,
    JsonResponse,
    HttpResponseRedirect,
    HttpResponseBadRequest,
)
from django.shortcuts import render, get_object_or_404, resolve_url
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.utils.translation import get_language
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import View

from acamar_api.forms import PositionSearchForm, CourseEnrollForm, PositionApplyForm
from acamar_api.models import Position
from .forms import ContactForm
from .models import Review, TeamGrid, PositionSearch


class ReviewApi(View):
    def get(self, request, id=None):
        if id:
            object = get_object_or_404(Review, pk=id, show=True)
            return render(
                request, "plugins/review_panel/review.html", {"object": object}
            )
        else:
            return HttpResponseNotAllowed([])


class PositionSearchApi(View):
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super(PositionSearchApi, self).dispatch(*args, **kwargs)

    def get(self, request, id):
        instance = get_object_or_404(PositionSearch, pk=id)
        form = PositionSearchForm(request.GET)
        if form.is_valid():
            sqs = form.search()
            return render(
                request,
                "plugins/position_search/results.html",
                {"instance": instance, "objects": sqs, "limit": instance.limit},
            )

        return HttpResponseBadRequest()


class PositionSearchAutocompleteApi(View):
    def get(self, request):
        sqs = Position.autocomplete(request.GET.get("q", "")).load_all()[:5]

        return render(
            request, "plugins/position_search/autocomplete.html", {"objects": sqs}
        )


class CourseEnrollApi(View):
    def post(self, request):
        form = CourseEnrollForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})

        return JsonResponse({"success": False, "data": form.errors})


@sensitive_post_parameters()
@csrf_protect
@never_cache
def login_api(request, redirect_field_name=REDIRECT_FIELD_NAME):
    redirect_to = request.POST.get(
        redirect_field_name, request.GET.get(redirect_field_name, "")
    )
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                acard = Page.objects.published().filter(reverse_id="a-card").first()
                redirect_to = acard.get_public_url() if acard else ""
                if not redirect_to:
                    redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            login(request, form.get_user())

            return JsonResponse({"success": True, "redirect": redirect_to})
        else:
            return JsonResponse({"success": False, "data": form.errors})
    else:
        login_page = Page.objects.published().filter(reverse_id="login").first()
        redirect = login_page.get_public_url() if login_page else ""
        if not redirect:
            redirect = "/login/"
        return HttpResponseRedirect(redirect + "?" + request.META["QUERY_STRING"])


class ContactApi(View):
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            return JsonResponse({"success": True})

        return JsonResponse({"success": False, "data": form.errors})


class PositionApi(View):
    def post(self, request):
        form = PositionApplyForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()

            return JsonResponse({"success": True})

        return JsonResponse({"success": False, "data": form.errors})
