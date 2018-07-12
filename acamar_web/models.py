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
    title = models.TextField(verbose_name="Title")
    subtitle = models.TextField(verbose_name="Sub-title")

    background_video = FilerVideoField(verbose_name="Background video", null=True, blank=True)
    background_image = FilerImageField(verbose_name="Background image", null=True, blank=True, help_text="Fallback for background video")

    def __str__(self):
        return truncatechars(self.title, 40)


@python_2_unicode_compatible
class MainBannerCard(CMSPlugin):
    title = models.TextField(verbose_name="Title")
    subtitle = models.TextField(verbose_name="Sub-title")
    button_link = PageField(verbose_name="Button link", on_delete=models.PROTECT)
    button_text = models.CharField(max_length=254, verbose_name="Button text")
    theme = models.CharField(choices=[("", "Black"), ("looking-for-gray", "Gray")], max_length=30, verbose_name="Theme", blank=True)

    def __str__(self):
        return self.title
