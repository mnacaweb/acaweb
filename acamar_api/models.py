# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json
import re

from cms.models import PlaceholderField
from django.conf import settings
from django.core.urlresolvers import reverse, NoReverseMatch
from django.db import models
from django.template.defaultfilters import date as dateformat
from django.utils import translation, timezone
from django.utils.encoding import python_2_unicode_compatible, force_text
from django.utils.functional import cached_property
from django.utils.text import slugify
from django.utils.translation import ugettext as _
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField
from haystack.query import SearchQuerySet
from meta.models import ModelMeta
from safedelete import SOFT_DELETE
from safedelete.models import SafeDeleteModel

from .utils import cv_upload_to


@python_2_unicode_compatible
class Course(ModelMeta, SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    title = models.CharField(verbose_name="Title", max_length=254)
    slug = models.SlugField(verbose_name="Url-slug")
    short_description = models.TextField(verbose_name="Short description")
    place = models.CharField(verbose_name="Place", max_length=254, blank=True)
    price = models.PositiveIntegerField(verbose_name="Price", blank=True, null=True)
    duration = models.CharField(verbose_name="Duration", max_length=254, blank=True)
    meta_title = models.CharField(verbose_name="Meta title", max_length=254, blank=True)
    meta_description = models.CharField(verbose_name="Meta description", max_length=254, blank=True)
    meta_keywords = models.CharField(verbose_name="Meta keywords", max_length=254, blank=True)
    main_banner = PlaceholderField("main_banner", related_name="course_main_banner")
    content = PlaceholderField("course_content", related_name="course_content")

    def __str__(self):
        return self.title

    _metadata = {
        'title': 'get_meta_title',
        'description': 'get_meta_description',
        'keywords': 'meta_keywords_list'
    }

    def get_meta_title(self):
        return self.meta_title if self.meta_title else self.title

    def get_meta_description(self):
        return self.meta_description if self.meta_description else self.short_description

    @cached_property
    def meta_keywords_list(self):
        return re.findall(r"[\w']+", self.meta_keywords)

    def get_absolute_url(self, language=None):
        language = language if language else translation.get_language()
        with translation.override(language):
            try:
                return reverse("course-detail", kwargs={"slug": self.slug})
            except NoReverseMatch:
                return "#"

    @cached_property
    def terms_comming(self):
        return self.terms.exclude(items__date__lt=timezone.now())

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


@python_2_unicode_compatible
class CourseTerm(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE

    course = models.ForeignKey("acamar_api.Course",
                               on_delete=models.CASCADE,
                               verbose_name="Course",
                               related_name="terms")

    def __str__(self):
        dates = map(lambda x: dateformat(x.date, "j.n.y"), self.items.all())
        return "{} - {}".format(self.course.title, " + ".join(dates) if dates else "--")

    class Meta:
        verbose_name = "Course term"
        verbose_name_plural = "Course terms"


@python_2_unicode_compatible
class CourseTermItem(models.Model):
    parent = models.ForeignKey("acamar_api.CourseTerm", on_delete=models.CASCADE, verbose_name="Course term",
                               related_name="items")
    date = models.DateField(verbose_name="Date")
    start_time = models.TimeField(verbose_name="Start time")
    end_time = models.TimeField(verbose_name="End time", null=True, blank=True)
    address = models.CharField(verbose_name="Address", max_length=254, blank=True)
    description = models.CharField(verbose_name="Description", max_length=254, blank=True)

    @property
    def time(self):
        if self.end_time:
            return "{}-{}".format(dateformat(self.start_time, "G.i"), dateformat(self.end_time, "G.i"))
        return dateformat(self.start_time, "G.i")

    def __str__(self):
        return "{} - {}".format(self.date, self.description)

    class Meta:
        verbose_name = "Course term - item"
        verbose_name_plural = "Course term - items"


@python_2_unicode_compatible
class CourseCache(object):
    def __init__(self, **kwargs):
        for key, value in kwargs.iteritems():
            setattr(self, key, value)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class PositionCategory(models.Model):
    name = models.CharField(verbose_name="Name", max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Position category"
        verbose_name_plural = "Position categories"


@python_2_unicode_compatible
class PositionPact(models.Model):
    name = models.CharField(verbose_name="Name", max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Position pact"
        verbose_name_plural = "Position pacts"


@python_2_unicode_compatible
class PositionTechnology(models.Model):
    name = models.CharField(verbose_name="Name", max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Position technology"
        verbose_name_plural = "Position technologies"


@python_2_unicode_compatible
class Position(ModelMeta, models.Model):
    internal_id = models.PositiveIntegerField(db_index=True)
    lang = models.CharField(max_length=3, choices=settings.LANGUAGES, db_index=True)
    date = models.DateTimeField()
    category = models.ForeignKey("acamar_api.PositionCategory", on_delete=models.CASCADE, related_name="positions")
    place = models.CharField(max_length=254, blank=True)
    start = models.CharField(max_length=254, blank=True)
    name = models.CharField(max_length=254, blank=True)
    slug = models.SlugField(blank=True, max_length=120)
    introduction = models.TextField(blank=True)
    title1 = models.CharField(max_length=254, blank=True)
    text1 = HTMLField(blank=True)
    title2 = models.CharField(max_length=254, blank=True)
    text2 = HTMLField(blank=True)
    title3 = models.CharField(max_length=254, blank=True)
    text3 = HTMLField(blank=True)
    title4 = models.CharField(max_length=254, blank=True)
    text4 = HTMLField(blank=True)
    title5 = models.CharField(max_length=254, blank=True)
    text5 = HTMLField(blank=True)
    title6 = models.CharField(max_length=254, blank=True)
    text6 = HTMLField(blank=True)
    user_email = models.CharField(max_length=254, blank=True)
    user_first_name = models.CharField(max_length=254, blank=True)
    user_second_name = models.CharField(max_length=254, blank=True)
    user_image = models.CharField(max_length=254, blank=True)
    _user_image_url = models.URLField(max_length=254, blank=True, db_column="user_image_url")
    user_phone = models.CharField(max_length=254, blank=True)
    user_position = models.CharField(max_length=254, blank=True)
    technologies = models.ManyToManyField("acamar_api.PositionTechnology", related_name="positions", blank=True)
    pacts = models.ManyToManyField("acamar_api.PositionPact", related_name="positions", blank=True)


    @classmethod
    def autocomplete(cls, term):
        return SearchQuerySet().autocomplete(autocomplete=term)

    @cached_property
    def pacts_text_array(self):
        return self.pacts.values_list("name", flat=True)

    @cached_property
    def pacts_array(self):
        return list(self.pacts.values_list("id", flat=True))

    @cached_property
    def pacts_json(self):
        return json.dumps(self.pacts_array)

    @cached_property
    def technologies_text(self):
        return ", ".join(self.technologies.values_list("name", flat=True))

    @cached_property
    def pacts_text(self):
        return ", ".join(self.pacts_text_array)

    @property
    def title(self):
        return self.name if self.name else self.title1 if self.title1 else ""

    def get_absolute_url(self, language=None):
        language = language if language else translation.get_language()
        if language != self.lang:
            translated = Position.objects.filter(internal_id=self.internal_id, lang=language).first()
            if translated:
                return translated.get_absolute_url(language)
            return "#"
        try:
            return reverse("position-detail", kwargs={"slug": self.slug})
        except NoReverseMatch:
            return "#"

    @property
    def url(self):
        return self.get_absolute_url()

    @cached_property
    def recruiter(self):
        return Recruiter.objects.filter(first_name=self.user_first_name, second_name=self.user_second_name).first()

    def get_recruiter_image_url(self):
        if self.recruiter:
            return self.recruiter.image.url
        return self.user_image_url

    @property
    def user_image_url(self):
        return self._user_image_url.replace("www", "old2018")

    def content_iterator(self):
        for index in range(1, 7):
            title = getattr(self, "title{}".format(index), "")
            text = getattr(self, "text{}".format(index), "")
            if title or text:
                yield {"title": title, "text": text}

    def __str__(self):
        return self.name if self.name else self.title1

    def _get_unique_slug(self):
        if self.title:
            slug = slugify(self.title)
            unique_slug = slug
            num = 1
            while Position.objects.filter(lang=self.lang, slug=unique_slug).exclude(id=self.id).exists():
                unique_slug = '{}-{}'.format(slug, num)
                num += 1
            return unique_slug
        return ""

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()

        super(Position, self).save(*args, **kwargs)

    def get_meta_title(self):
        return "{} — Acamar".format(self.name)

    def get_meta_description(self):
        return _("Příjmi nový IT projekt jako svoji výzvu. Získej odměnu, zkušenosti a posuň se dál! Pracuj s českými i mezinárodními týmy.")

    _metadata = {
        'title': 'get_meta_title',
        'description': 'get_meta_description',
    }

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"
        unique_together = ("lang", "internal_id")


@python_2_unicode_compatible
class CourseEnroll(models.Model):
    name = models.CharField(verbose_name="Name", max_length=254)
    phone = models.CharField(verbose_name="Phone", max_length=20)
    email = models.EmailField(verbose_name="Email", max_length=254)
    courses = models.ManyToManyField("acamar_api.CourseTerm", related_name="enrolled", verbose_name="Course terms")
    expectations = models.TextField(verbose_name="Expectations", blank=True)
    cv = models.FileField(verbose_name="CV", upload_to=cv_upload_to, null=True, blank=True)
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)

    @cached_property
    def course_list(self):
        return ",".join(Course.objects.filter(terms__in=self.courses.all()).values_list("title", flat=True))

    @cached_property
    def course_terms(self):
        terms = [force_text(x) for x in self.courses.all()]
        return ", ".join(terms)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Course registration"
        verbose_name_plural = "Course registrations"


@python_2_unicode_compatible
class PositionApply(models.Model):
    position = models.ForeignKey("acamar_api.Position", verbose_name="Position", blank=True, null=True, on_delete=models.SET_NULL)
    position_name = models.CharField(verbose_name="Position - name", max_length=254)
    position_user_name = models.CharField(verbose_name="Position - person", max_length=254)
    position_user_email = models.EmailField(verbose_name="Position - person email", max_length=254)
    first_name = models.CharField(verbose_name="First name", max_length=254)
    last_name = models.CharField(verbose_name="Last name", max_length=254)
    email = models.EmailField(verbose_name="Email", max_length=254)
    phone = models.CharField(verbose_name="Phone", max_length=20)
    cv = models.FileField(verbose_name="CV", upload_to=cv_upload_to, null=True, blank=True)
    linkedin = models.URLField(verbose_name="LinkedIn", max_length=254, blank=True)
    text = models.TextField(verbose_name="Text", blank=True)
    created = models.DateTimeField(verbose_name="Created", auto_now_add=True)

    def __str__(self):
        return "{} {} - {}".format(self.first_name, self.last_name, self.position_name)

    class Meta:
        verbose_name = "Position application"
        verbose_name_plural = "Position application"

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.position:
            self.position_name = self.position.name
            self.position_user_name = "{} {}".format(self.position.user_first_name, self.position.user_second_name)
            self.position_user_email = self.position.user_email
        super(PositionApply, self).save(force_insert, force_update, using, update_fields)


@python_2_unicode_compatible
class Recruiter(models.Model):
    first_name = models.CharField(verbose_name="First name", max_length=255)
    second_name = models.CharField(verbose_name="Second name", max_length=255)
    image = FilerImageField(verbose_name="Image", on_delete=models.PROTECT)

    def __str__(self):
        return "{} {}".format(self.first_name, self.second_name)

    class Meta:
        verbose_name = "Recruiter"
        verbose_name_plural = "Recruiters"
        unique_together = ("first_name", "second_name")
