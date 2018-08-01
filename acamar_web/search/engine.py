# coding=utf-8
from __future__ import print_function

from haystack.backends.whoosh_backend import WhooshEngine, WhooshSearchBackend
from whoosh.analysis import CharsetFilter
from whoosh.fields import TEXT, NGRAMWORDS
from whoosh.support.charset import accent_map


class FoldingWhooshSearchBackend(WhooshSearchBackend):
    def build_schema(self, fields):
        schema = super(FoldingWhooshSearchBackend, self).build_schema(fields)

        for name, field in schema[1].items():
            if isinstance(field, TEXT) or isinstance(field, NGRAMWORDS):
                field.analyzer.items.append(CharsetFilter(accent_map))

        return schema


class FoldingWhooshEngine(WhooshEngine):
    backend = FoldingWhooshSearchBackend
