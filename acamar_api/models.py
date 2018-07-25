import re

from cms.models import PlaceholderField
from django.core.urlresolvers import reverse, NoReverseMatch
from django.db import models
from django.utils import translation
from django.utils.encoding import python_2_unicode_compatible
from django.utils.functional import cached_property
from django.utils.text import slugify
from djangocms_text_ckeditor.fields import HTMLField
from haystack.query import SearchQuerySet
from meta.models import ModelMeta


@python_2_unicode_compatible
class Course(ModelMeta, models.Model):
    title = models.CharField(verbose_name="Title", max_length=254)
    slug = models.SlugField(verbose_name="Url-slug", unique=True)
    short_description = models.TextField(verbose_name="Short description")
    place = models.CharField(verbose_name="Place", max_length=254, blank=True)
    price = models.PositiveIntegerField(verbose_name="Price", blank=True, null=True)
    duration = models.CharField(verbose_name="Duration", max_length=254, blank=True)
    meta_keywords = models.CharField(verbose_name="Meta keywords", max_length=254, blank=True)
    main_banner = PlaceholderField("main_banner", related_name="course_main_banner")
    content = PlaceholderField("course_content", related_name="course_content")

    def __str__(self):
        return self.title

    _metadata = {
        'title': 'title',
        'description': 'short_description',
        'keywords': 'meta_keywords_list'
    }

    @cached_property
    def meta_keywords_list(self):
        return re.findall(r"[\w']+", self.meta_keywords)

    def get_absolute_url(self, language=translation.get_language()):
        with translation.override(language):
            try:
                return reverse("course-detail", kwargs={"slug": self.slug})
            except NoReverseMatch:
                return "#"

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


@python_2_unicode_compatible
class CourseTerm(models.Model):
    course = models.ForeignKey("acamar_api.Course", on_delete=models.CASCADE, verbose_name="Course")

    def __str__(self):
        return "{} - {}".format(self.course.title, getattr(self.items.first(), "date", "--"))

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
    lang = models.BooleanField(default=False, db_index=True)
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
    user_image_url = models.URLField(max_length=254, blank=True)
    user_phone = models.CharField(max_length=254, blank=True)
    user_position = models.CharField(max_length=254, blank=True)
    technologies = models.ManyToManyField("acamar_api.PositionTechnology", related_name="positions")
    pacts = models.ManyToManyField("acamar_api.PositionPact", related_name="positions")

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
    def technologies_text(self):
        return ", ".join(self.technologies.values_list("name", flat=True))

    @property
    def title(self):
        return self.name if self.name else self.title1 if self.title1 else "--"

    def get_absolute_url(self, language=translation.get_language()):
        with translation.override(language):
            if self.lang:
                try:
                    return reverse("position-detail", kwargs={"slug": self.slug})
                except NoReverseMatch:
                    return "#"
            else:
                return "#"

    @property
    def url(self):
        return self.get_absolute_url()

    def content_iterator(self):
        for index in range(1, 7):
            title = getattr(self, "title{}".format(index), "")
            text = getattr(self, "text{}".format(index), "")
            if title or text:
                yield {"title": title, "text": text}

    def __str__(self):
        return self.name if self.name else self.title1

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        num = 1
        while Position.objects.filter(slug=unique_slug).exclude(id=self.id).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super(Position, self).save(*args, **kwargs)

    _metadata = {
        'description': 'title',
    }

    class Meta:
        verbose_name = "Position"
        verbose_name_plural = "Positions"
