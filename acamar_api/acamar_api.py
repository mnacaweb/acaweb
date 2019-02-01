# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import warnings

import requests
from dateutil import parser as dateparser
from django.conf import settings
from django.core.cache import cache
from django.core.management import call_command
from django.utils import translation, timezone
from django.utils.termcolors import colorize

from .models import PositionCategory, PositionPact, Position, PositionTechnology, CourseCache


class AcamarCourseManager:
    model = CourseCache
    cache_prefix = "acamar_course_{}"
    cache_duration = 300

    @classmethod
    def all(cls, cached=True):
        warnings.warn(colorize("Deprecated", fg="red"), DeprecationWarning, stacklevel=2)
        cache_key = cls.cache_prefix.format("all")
        courses = cache.get(cache_key) if cached else None
        if not courses:
            courses = cls._all()
            cache.set(cache_key, courses, cls.cache_duration)
        return courses

    @classmethod
    def all_list(cls, cached=True):
        return cls.all(cached).values()

    @classmethod
    def _all(cls):
        resp = requests.get(url="https://old2018.acamar.cz/api_kurzy.php",
                            params={"token": "ad9078ccdc3ac86598a770b2e6fb7ca6"},
                            proxies=settings.PROXIES, verify=False)
        if resp.status_code == 200:
            json = resp.json()
            courses = {}
            for id, course in json.iteritems():
                courses[id] = cls.model(**course)
            return courses
        else:
            return {}

    @classmethod
    def get_by_id(cls, id, cached=True):
        courses = cls.all(cached)
        return courses[str(id)]

    @classmethod
    def get_choices(cls, cached=True):
        courses = cls.all(cached)
        return [(int(id), obj.title) for id, obj in courses.iteritems()]


class AcamarPositionManager:
    url = "https://old2018.acamar.cz/api_pozice.php"
    cache_prefix = "acamar_position_{}"
    cache_duration = 300

    @classmethod
    def _request(cls, lng):
        resp = requests.get(url=cls.url,
                            params={"token": "ace247464bfa9076dada655abea751c6", "lng": lng},
                            proxies=settings.PROXIES, verify=False)
        if resp.status_code == 200:
            return resp.json()

    @classmethod
    def get_data(cls, lng, cached=True):
        cache_key = cls.cache_prefix.format(lng)
        data = cache.get(cache_key) if cached else None
        if data is None:
            data = cls._request(lng)
            cache.set(cache_key, data, cls.cache_duration)
        return data

    @classmethod
    def get_categories(cls, lng):
        data = cls.get_data(lng)
        return data.get("kategorie", [])

    @classmethod
    def sync_categories(cls):
        for language, _ in settings.LANGUAGES:
            with translation.override(language):
                for category in cls.get_categories(language):
                    PositionCategory.objects.update_or_create(id=category["id"],
                                                              defaults={"name": category["category"]})

    @classmethod
    def get_pacts(cls, lng):
        data = cls.get_data(lng)
        return data.get("uvazek", [])

    @classmethod
    def sync_pacts(cls):
        for language, _ in settings.LANGUAGES:
            with translation.override(language):
                for pact in cls.get_pacts(language):
                    PositionPact.objects.update_or_create(id=pact["id"], defaults={"name": pact["short"]})

    @classmethod
    def get_technologies(cls, lng):
        data = cls.get_data(lng)
        return data.get("technologie", [])

    @classmethod
    def sync_technologies(cls):
        for language, _ in settings.LANGUAGES:
            with translation.override(language):
                for technology in cls.get_technologies(language):
                    PositionTechnology.objects.update_or_create(id=technology["id"],
                                                                defaults={"name": technology["short"]})

    @classmethod
    def get_positions(cls, lng):
        data = cls.get_data(lng)
        return data.get("inzerat", [])

    @classmethod
    def sync_positions(cls):
        obj_ids = []
        for language, _ in settings.LANGUAGES:
            with translation.override(language):
                for position in cls.get_positions(language):
                    user = position.get("__user", {})
                    technologies = [key for key, value in position.get("__technologie", {}).iteritems() if value]
                    pacts = [key for key, value in position.get("__uvazek", {}).iteritems() if value]
                    obj, _ = Position.objects.update_or_create(internal_id=position["id"], lang=language,
                                                               defaults={
                        "date": dateparser.parse(position["date"]).replace(tzinfo=timezone.utc),
                        "category_id": position["kategorie"],
                        "place": position["misto_vykonu_prace"],
                        "start": position["nastup"],
                        "name": position["nazev_acamar"],
                        "introduction": position["uvod_acamar"],
                        "title1": position["titulek1"],
                        "text1": position["text1"],
                        "title2": position["titulek2"],
                        "text2": position["text2"],
                        "title3": position["titulek3"],
                        "text3": position["text3"],
                        "title4": position["titulek4"],
                        "text4": position["text4"],
                        "title5": position["titulek5"],
                        "text5": position["text5"],
                        "title6": position["titulek6"],
                        "text6": position["text6"],
                        "user_email": user["email"],
                        "user_first_name": user["firstName"],
                        "user_second_name": user["secondName"],
                        "user_image": user["image"],
                        "_user_image_url": user["image_url"],
                        "user_phone": user["telefon"],
                        "user_position": user["pozice"],
                    })
                    obj.pacts.clear()
                    obj.pacts.add(*pacts)
                    obj.technologies.clear()
                    obj.technologies.add(*technologies)
                    obj_ids.append(obj.id)

        return Position.objects.all().exclude(id__in=obj_ids).delete()

    @classmethod
    def sync(cls):
        start = timezone.now()
        print("POSITION SYNC - START - {}".format(start.strftime("%d.%m.%Y %H:%M:%S")))
        cls.sync_categories()
        cls.sync_technologies()
        cls.sync_pacts()
        cls.sync_positions()
        end = timezone.now()
        print("POSITION SYNC - FINISH - {} - EST:{}".format(end.strftime("%d.%m.%Y %H:%M:%S"), end-start))
