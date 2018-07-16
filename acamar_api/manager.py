# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import requests
from django.core.cache import cache
from django.utils.termcolors import colorize

from .models import Course


class AcamarCourseManager:
    model = Course
    cache_prefix = "acamar_course_{}"
    cache_duration = 300

    @classmethod
    def all(cls, cached=True):
        cache_key = cls.cache_prefix.format("all")
        courses = cache.get(cache_key) if cached else None
        if courses is None:
            courses = cls._all()
            cache.set(cache_key, courses, cls.cache_duration)
        else:
            print(colorize("CACHE HIT - {}".format(cache_key), fg="red"))
        return courses

    @classmethod
    def _all(cls):
        resp = requests.get(url="https://www.acamar.cz/api_kurzy.php", params={"token": "ad9078ccdc3ac86598a770b2e6fb7ca6"})
        if resp.status_code == 200:
            json = resp.json()
            courses = []
            for id, course in json.iteritems():
                courses.append(cls.model(**course))
            return courses