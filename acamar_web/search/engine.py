import haystack
from elasticsearch import NotFoundError
from haystack.backends.elasticsearch5_backend import Elasticsearch5SearchBackend
from haystack.backends.elasticsearch5_backend import Elasticsearch5SearchEngine
from haystack.backends.elasticsearch_backend import DEFAULT_FIELD_MAPPING, FIELD_MAPPINGS
from haystack.constants import DJANGO_CT, DJANGO_ID


class FixedElasticsearch5SearchBackend(Elasticsearch5SearchBackend):
    def setup(self):
        """
        Defers loading until needed.
        """
        # Get the existing mapping & cache it. We'll compare it
        # during the ``update`` & if it doesn't match, we'll put the new
        # mapping.
        self.silently_fail = False
        try:
            self.existing_mapping = self.conn.indices.get_mapping(
                index=self.index_name, ignore=404
            )
        except NotFoundError:
            pass
        except Exception:
            if not self.silently_fail:
                raise

        unified_index = haystack.connections[self.connection_alias].get_unified_index()
        self.content_field_name, field_mapping = self.build_schema(
            unified_index.all_searchfields()
        )
        current_mapping = {"modelresult": {"properties": field_mapping}}

        if current_mapping != self.existing_mapping:
            try:
                # Make sure the index is there first.
                self.conn.indices.create(
                    index=self.index_name, body=self.DEFAULT_SETTINGS, ignore=400
                )
                self.conn.indices.put_mapping(
                    index=self.index_name, doc_type="modelresult", body=current_mapping
                )
                self.existing_mapping = current_mapping
            except Exception:
                if not self.silently_fail:
                    raise

        self.setup_complete = True


class Elasticsearch5SearchBackendCz(FixedElasticsearch5SearchBackend):
    DEFAULT_SETTINGS = {
        "settings": {
            "max_ngram_diff": 7,
            "index": {"number_of_shards": 4, "number_of_replicas": 0},
            "analysis": {
                "analyzer": {
                    "ngram_analyzer": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": [
                            "cs_stopwords",
                            "cs_hunspell",
                            "lowercase",
                            "cs_stopwords",
                            "icu_folding",
                            "remove_duplicates",
                            "haystack_ngram",
                        ],
                    },
                    "edgengram_analyzer": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": [
                            "cs_stopwords",
                            "cs_hunspell",
                            "lowercase",
                            "cs_stopwords",
                            "icu_folding",
                            "remove_duplicates",
                            "haystack_edgengram",
                        ],
                    },
                    "pb_analyzer": {
                        "type": "custom",
                        "tokenizer": "standard",
                        "filter": [
                            "cs_stopwords",
                            "cs_hunspell",
                            "lowercase",
                            "cs_stopwords",
                            "icu_folding",
                            "remove_duplicates",
                        ],
                        # "char_filter": ["html_strip"]
                    },
                },
                "tokenizer": {
                    "haystack_ngram_tokenizer": {
                        "type": "nGram",
                        "min_gram": 3,
                        "max_gram": 10,
                    },
                    "haystack_edgengram_tokenizer": {
                        "type": "edgeNGram",
                        "min_gram": 3,
                        "max_gram": 10,
                        "side": "front",
                    },
                },
                # "char_filter": {
                #     "my_html_strip": {
                #         "type": "html_strip",
                #         "escaped_tags": []
                #     }
                # },
                "filter": {
                    "haystack_ngram": {"type": "nGram", "min_gram": 3, "max_gram": 10},
                    "haystack_edgengram": {
                        "type": "edgeNGram",
                        "min_gram": 3,
                        "max_gram": 10,
                    },
                    "cs_stopwords": {
                        "type": "stop",
                        "stopwords": "_czech_",
                        "ignore_case": True,
                    },
                    "cs_hunspell": {
                        "type": "hunspell",
                        "locale": "cs_CZ",
                        "dedup": True,
                        "recursion_level": 2,
                    },
                    "cs_stemmer": {"type": "stemmer", "language": "czech"},
                    "remove_duplicates": {
                        "type": "unique",
                        "only_on_same_position": True,
                    },
                },
            },
        }
    }

    def build_schema(self, fields):
        content_field_name = ""
        mapping = {
            DJANGO_CT: {"type": "text", "index": False},
            DJANGO_ID: {"type": "text", "index": False},
        }

        CUSTOM_FIELD_MAPPING = {"type": "text", "analyzer": "pb_analyzer"}

        for field_name, field_class in fields.items():
            field_mapping = FIELD_MAPPINGS.get(
                field_class.field_type, CUSTOM_FIELD_MAPPING
            ).copy()
            if field_class.boost != 1.0:
                field_mapping["boost"] = field_class.boost

            if field_class.document is True:
                content_field_name = field_class.index_fieldname

            if field_mapping["type"] == "text" or field_mapping["type"] == "string":
                field_mapping["type"] = "text"
                if field_class.indexed is False or hasattr(field_class, "facet_for"):
                    field_mapping["index"] = False
                    del field_mapping["analyzer"]

            mapping[field_class.index_fieldname] = field_mapping

        return content_field_name, mapping


class Elasticsearch5SearchEngineCz(Elasticsearch5SearchEngine):
    backend = Elasticsearch5SearchBackendCz


class Elasticsearch5SearchBackendRu(FixedElasticsearch5SearchBackend):
    def build_schema(self, fields):
        content_field_name = ""
        mapping = {
            DJANGO_CT: {"type": "text", "index": False},
            DJANGO_ID: {"type": "text", "index": False},
        }

        CUSTOM_FIELD_MAPPING = {"type": "text", "analyzer": "russian"}

        for field_name, field_class in fields.items():
            field_mapping = FIELD_MAPPINGS.get(
                field_class.field_type, CUSTOM_FIELD_MAPPING
            ).copy()
            if field_class.boost != 1.0:
                field_mapping["boost"] = field_class.boost

            if field_class.document is True:
                content_field_name = field_class.index_fieldname

            # Do this last to override `text` fields.
            if field_mapping["type"] == "text" or field_mapping["type"] == "string":
                field_mapping["type"] = "text"
                if field_class.indexed is False or hasattr(field_class, "facet_for"):
                    field_mapping["index"] = "not_analyzed"
                    del field_mapping["analyzer"]

            mapping[field_class.index_fieldname] = field_mapping

        return content_field_name, mapping


class Elasticsearch5SearchEngineRu(Elasticsearch5SearchEngine):
    backend = Elasticsearch5SearchBackendRu


class Elasticsearch5SearchBackendEn(FixedElasticsearch5SearchBackend):
    def build_schema(self, fields):
        content_field_name = ""
        mapping = {
            DJANGO_CT: {"type": "text", "index": False},
            DJANGO_ID: {"type": "text", "index": False},
        }

        for field_name, field_class in fields.items():
            field_mapping = FIELD_MAPPINGS.get(
                field_class.field_type, DEFAULT_FIELD_MAPPING
            ).copy()
            if field_class.boost != 1.0:
                field_mapping["boost"] = field_class.boost

            if field_class.document is True:
                content_field_name = field_class.index_fieldname

            # Do this last to override `text` fields.
            if field_mapping["type"] == "text" or field_mapping["type"] == "string":
                field_mapping["type"] = "text"
                if field_class.indexed is False or hasattr(field_class, "facet_for"):
                    field_mapping["index"] = "not_analyzed"
                    del field_mapping["analyzer"]

            mapping[field_class.index_fieldname] = field_mapping

        return content_field_name, mapping


class Elasticsearch5SearchEngineEn(Elasticsearch5SearchEngine):
    backend = Elasticsearch5SearchBackendEn
