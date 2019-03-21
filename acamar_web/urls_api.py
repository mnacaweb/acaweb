# -*- coding: utf-8 -*-
from django.urls import path

from .api import ReviewApi, PositionSearchApi, PositionSearchAutocompleteApi, CourseEnrollApi, login_api, \
    ContactApi, PositionApi

app_name = 'acamar_web'
urlpatterns = [
    path('reviews/', ReviewApi.as_view(), name="reviews"),
    path('reviews/<int:id>/', ReviewApi.as_view(), name="reviews"),

    path('position_search/', PositionSearchAutocompleteApi.as_view(), name="position-search-autocomplete"),
    path('position_search/<int:id>/', PositionSearchApi.as_view(), name="position-search"),

    path('course_enroll/', CourseEnrollApi.as_view(), name="course-enroll"),

    path('login/', login_api, name="login"),

    path('contact/', ContactApi.as_view(), name="contact"),

    path('position/', PositionApi.as_view(), name="position")
]
