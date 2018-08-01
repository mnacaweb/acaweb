# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms
from haystack.forms import SearchForm

from .models import Position, CourseEnroll, PositionApply


class PositionSearchForm(SearchForm):
    def search(self):
        if not self.is_valid():
            return self.no_query_found()

        sqs = self.searchqueryset.auto_query(self.cleaned_data['q'])

        if self.load_all:
            sqs = sqs.load_all()

        return sqs.models(Position)


class CourseEnrollForm(forms.ModelForm):
    class Meta:
        model = CourseEnroll
        fields = ["name", "phone", "courses", "expectations", "cv"]


class PositionApplyForm(forms.ModelForm):
    class Meta:
        model = PositionApply
        fields = ["position", "first_name", "last_name", "email", "phone", "cv", "linkedin", "text"]