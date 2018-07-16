# coding: utf-8

from __future__ import unicode_literals

import os

from cms.models import CMSPlugin
from cms.models.fields import PageField
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext as _
from filer.fields.image import FilerImageField
from filer.models import File


class FilerVideo(File):
    _icon = "video"

    @classmethod
    def matches_file_type(cls, name, file, request):
        # the extensions we'll recognise for this file type
        filename_extensions = ['.mp4', '.webm', '.ogg']
        ext = os.path.splitext(name)[1].lower()
        return ext in filename_extensions


from .fields import FilerVideoField


@python_2_unicode_compatible
class MainBanner(CMSPlugin):
    DEFAULT = "default"
    CANDIDATES = "candidates"
    WE_ARE = "we_are"
    COURSE = "course"
    CONTACT = "contact"
    DETAIL = "detail"
    _CHOICES = [
        (DEFAULT, "Default"),
        (CANDIDATES, "Candidates"),
        (WE_ARE, "We are"),
        (COURSE, "Course"),
        (CONTACT, "Contact"),
        (DETAIL, "Detail")
    ]

    template = models.CharField(verbose_name="Template", max_length=100, choices=_CHOICES, default=DEFAULT)
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.TextField(verbose_name="Sub-title")

    background_video = FilerVideoField(verbose_name="Background video", null=True, blank=True, related_name="main_banners_video")
    background_image = FilerImageField(verbose_name="Background image", null=True, blank=True, help_text="Fallback for background video", related_name="main_banners_image")

    def __str__(self):
        return truncatechars(self.title, 40)


@python_2_unicode_compatible
class MainBannerCard(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.TextField(verbose_name="Sub-title")
    button_link = PageField(verbose_name="Button link", on_delete=models.PROTECT)
    button_text = models.CharField(max_length=254, verbose_name="Button text")
    theme = models.CharField(choices=[("", "Black"), ("looking-for-gray", "Gray")], max_length=30, verbose_name="Theme", blank=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class WorkElipseColumn(models.Model):
    parent = models.ForeignKey("acamar_web.WorkElipse", on_delete=models.CASCADE, related_name="columns")
    image = FilerImageField(verbose_name="Image", on_delete=models.PROTECT, related_name="work_elipse_columns")
    title = models.CharField(verbose_name="Title", max_length=254)
    text = models.TextField(verbose_name="Text")

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class WorkElipse(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)

    def copy_relations(self, old_instance):
        self.columns.all().delete()

        for column in old_instance.columns.all():
            column.pk = None
            column.parent = self
            column.save()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Review(models.Model):
    author = models.CharField(verbose_name="Author", max_length=254)
    text = models.TextField(verbose_name="Text")
    image = FilerImageField(verbose_name="Image", on_delete=models.PROTECT, blank=True, null=True, related_name="reviews_image")
    logo = FilerImageField(verbose_name="Logo", on_delete=models.PROTECT, blank=True, null=True, related_name="reviews_logo")
    show = models.BooleanField(verbose_name="Show", default=True, db_index=True)

    def __str__(self):
        return "{}: {}".format(self.author, truncatechars(self.text, 30))

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"


@python_2_unicode_compatible
class ReviewPanel(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.TextField(verbose_name="Sub-title")
    positions_pretext = models.CharField(verbose_name="Positions - pre-text", max_length=254)
    positions_number = models.PositiveSmallIntegerField(verbose_name="Positions - number")
    positions_posttext = models.CharField(verbose_name="Positions - post-text", max_length=254)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Teamwork(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    button_link = PageField(verbose_name="Button link", on_delete=models.PROTECT)
    button_text = models.CharField(verbose_name="Button text", max_length=254)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class TeamworkLogo(CMSPlugin):
    image = FilerImageField(verbose_name="Image", related_name="teamwork_logos", on_delete=models.PROTECT)

    def __str__(self):
        return self.image.path.rsplit("/")[-1]
