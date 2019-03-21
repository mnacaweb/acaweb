from haystack.backends.elasticsearch5_backend import Elasticsearch5SearchBackend
from haystack.backends.elasticsearch5_backend import Elasticsearch5SearchEngine
from haystack.backends.elasticsearch_backend import FIELD_MAPPINGS
from haystack.constants import DJANGO_CT, DJANGO_ID


class Elasticsearch5SearchBackendCz(Elasticsearch5SearchBackend):
    DEFAULT_SETTINGS = {
        "settings": {
            # "index": {
            #     "number_of_shards": 4,
            #     "number_of_replicas": 0
            # },
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
                        "max_gram": 15,
                    },
                    "haystack_edgengram_tokenizer": {
                        "type": "edgeNGram",
                        "min_gram": 2,
                        "max_gram": 15,
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
                    "haystack_ngram": {"type": "nGram", "min_gram": 3, "max_gram": 15},
                    "haystack_edgengram": {
                        "type": "edgeNGram",
                        "min_gram": 2,
                        "max_gram": 15,
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
            }
        }
    }

    # get from parent and lightli modified
    def build_schema(self, fields):
        content_field_name = ""
        mapping = {
            DJANGO_CT: {
                "type": "text",
                "index": "not_analyzed",
                "include_in_all": False,
            },
            DJANGO_ID: {
                "type": "text",
                "index": "not_analyzed",
                "include_in_all": False,
            },
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

            # Do this last to override `text` fields.
            if field_mapping["type"] == "text" or field_mapping["type"] == "string":
                field_mapping["type"] = "text"
                if field_class.indexed is False or hasattr(field_class, "facet_for"):
                    field_mapping["index"] = "not_analyzed"
                    del field_mapping["analyzer"]

            mapping[field_class.index_fieldname] = field_mapping

        return content_field_name, mapping


class Elasticsearch5SearchEngineCz(Elasticsearch5SearchEngine):
    backend = Elasticsearch5SearchBackendCz


class Elasticsearch5SearchBackendRu(Elasticsearch5SearchBackend):
    def build_schema(self, fields):
        content_field_name = ""
        mapping = {
            DJANGO_CT: {
                "type": "text",
                "index": "not_analyzed",
                "include_in_all": False,
            },
            DJANGO_ID: {
                "type": "text",
                "index": "not_analyzed",
                "include_in_all": False,
            },
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
