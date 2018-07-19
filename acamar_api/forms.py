# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from haystack.forms import SearchForm

from .models import Position


class PositionSearchForm(SearchForm):
    def search(self):
        if not self.is_valid():
            return self.no_query_found()

        sqs = self.searchqueryset.auto_query(self.cleaned_data['q'])

        if self.load_all:
            sqs = sqs.load_all()

        return sqs.models(Position)
