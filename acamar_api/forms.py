# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from haystack.forms import SearchForm

from .models import Position


class PositionSearchForm(SearchForm):
    def search(self):
        sqs = super(PositionSearchForm, self).search()
        return sqs.models(Position)
