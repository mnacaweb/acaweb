# coding: utf-8

from __future__ import unicode_literals

import os
import urllib

from adminsortable.models import SortableMixin
from cms.models import CMSPlugin
from cms.models.fields import PageField
from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils.encoding import python_2_unicode_compatible
from django.utils.functional import cached_property, lazy
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField
from filer.models import File

from acamar_api.manager import AcamarCourseManager


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
    FOR_CANDIDATES = "for_candidates"
    FOR_COMPANIES = "for_companies"
    WE_ARE = "we_are"
    COURSE = "course"
    CONTACT = "contact"
    DETAIL = "detail"
    _CHOICES = [
        (DEFAULT, "Default"),
        (FOR_CANDIDATES, "For candidates"),
        (FOR_COMPANIES, "For companies"),
        (WE_ARE, "We are"),
        (COURSE, "Course"),
        (CONTACT, "Contact"),
        (DETAIL, "Detail")
    ]

    template = models.CharField(verbose_name="Template", max_length=100, choices=_CHOICES, default=DEFAULT)
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.TextField(verbose_name="Sub-title", blank=True)

    background_video = FilerVideoField(verbose_name="Background video", null=True, blank=True,
                                       related_name="main_banners_video")
    background_image = FilerImageField(verbose_name="Background image", null=True, blank=True,
                                       help_text="Fallback for background video", related_name="main_banners_image")

    def __str__(self):
        return truncatechars(self.title, 40)


@python_2_unicode_compatible
class MainBannerCard(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.TextField(verbose_name="Sub-title")
    button_link = PageField(verbose_name="Button link", on_delete=models.PROTECT)
    button_text = models.CharField(max_length=254, verbose_name="Button text")
    theme = models.CharField(choices=[("", "Black"), ("looking-for-gray", "Gray")], max_length=30, verbose_name="Theme",
                             blank=True)

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
    image = FilerImageField(verbose_name="Image", on_delete=models.PROTECT, blank=True, null=True,
                            related_name="reviews_image")
    logo = FilerImageField(verbose_name="Logo", on_delete=models.PROTECT, blank=True, null=True,
                           related_name="reviews_logo")
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
class LogoPanel(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    button_link = PageField(verbose_name="Button link", on_delete=models.PROTECT)
    button_text = models.CharField(verbose_name="Button text", max_length=254)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Logo(CMSPlugin):
    image = FilerImageField(verbose_name="Image", related_name="teamwork_logos", on_delete=models.PROTECT)

    def __str__(self):
        return self.image.path.rsplit("/")[-1]


@python_2_unicode_compatible
class CoursePanel(CMSPlugin):
    DEFAULT = ""
    ALTERNATIVE = "_alternative"
    _TEMPLATE_OPTIONS = [
        (DEFAULT, "Default"),
        (ALTERNATIVE, "Alternative with background")
    ]

    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.CharField(verbose_name="Sub-title", max_length=254)
    template = models.CharField(verbose_name="Template", max_length=20, choices=_TEMPLATE_OPTIONS, blank=True, default=DEFAULT)
    text = models.TextField(verbose_name="Text")
    button_text = models.CharField(verbose_name="Button text", max_length=254, blank=True)
    button_link_external = models.URLField(
        verbose_name='External link',
        blank=True,
        max_length=2040,
        help_text='Provide a valid URL to an external website.',
    )
    button_link_internal = PageField(
        verbose_name='Internal link',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text='If provided, overrides the external link.',
    )

    @property
    def button_link(self):
        if self.button_link_internal:
            return self.button_link_internal.get_absolute_url()
        elif self.button_link_external:
            return self.button_link_external
        else:
            return ""

    def __str__(self):
        return self.title

    def courses(self):
        items = self.items.all()
        if items:
            return [item.course for item in items]
        return AcamarCourseManager.all_list()

    def copy_relations(self, old_instance):
        self.items.all().delete()

        for item in old_instance.items.all():
            item.pk = None
            item.parent = self
            item.save()


@python_2_unicode_compatible
class CoursePanelItem(models.Model):
    course_panel = models.ForeignKey("acamar_web.CoursePanel", on_delete=models.CASCADE, related_name="items")
    _course = models.PositiveIntegerField(verbose_name="Course", choices=[])

    def __init__(self, *args, **kwargs):
        super(CoursePanelItem, self).__init__(*args, **kwargs)
        self._meta.get_field_by_name('_course')[0]._choices = lazy(AcamarCourseManager.get_choices, list)()

    @cached_property
    def course(self):
        return AcamarCourseManager.get_by_id(self._course)

    def __str__(self):
        return self.course.title

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


@python_2_unicode_compatible
class CreateTeam(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.TextField(verbose_name="Sub-title")

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class CreateTeamCard(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.CharField(verbose_name="Sub-title", max_length=254)
    image = FilerImageField(verbose_name="Image", on_delete=models.PROTECT)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class TeamGrid(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.TextField(verbose_name="Sub-title")
    button_text = models.CharField(verbose_name="Button text", max_length=254)
    limit = models.PositiveSmallIntegerField(verbose_name="Limit count", null=True, blank=True)

    def _members(self):
        return TeamMember.objects.all()

    @cached_property
    def members_limited(self):
        return self._members()[:self.limit] if self.limit else self._members()

    @cached_property
    def members_lazy(self):
        return self._members()[self.limit:] if self.limit else []

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class TeamMember(SortableMixin):
    name = models.CharField(verbose_name="Name", max_length=254)
    nickname = models.CharField(verbose_name="Position / Nickname", max_length=254)
    text = models.TextField(verbose_name="Text")
    image = FilerImageField(verbose_name="Image", on_delete=models.PROTECT)

    order = models.PositiveIntegerField(default=0, editable=False, db_index=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Team member"
        verbose_name_plural = "Team members"
        ordering = ["order"]


@python_2_unicode_compatible
class ContactGrid(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class ContactCard(CMSPlugin):
    name = models.CharField(verbose_name="Name", max_length=254)
    title = models.CharField(verbose_name="Title", max_length=254)
    image = FilerImageField(verbose_name="Image", on_delete=models.PROTECT)
    text = models.TextField(verbose_name="Text")
    phone = models.CharField(verbose_name="Phone", blank=True, max_length=20)
    email = models.EmailField(verbose_name="Email", blank=True)
    linkedin = models.URLField(verbose_name="LinedIn URL", blank=True)

    def __str__(self):
        return self.name

    @property
    def linkedin_formatted(self):
        link = urllib.unquote_plus(self.linkedin.encode("utf-8")).decode("utf-8").split("://", 1)[1]
        if link.startswith("www."):
            return link[4:]
        return link


@python_2_unicode_compatible
class ContactFormPurposeOption(models.Model):
    form = models.ForeignKey("acamar_web.ContactFormModel", on_delete=models.CASCADE, related_name="purpose_options",
                             editable=False)
    name = models.CharField(verbose_name="Option name", max_length=254)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Purpose option"
        verbose_name_plural = "Purpose options"


@python_2_unicode_compatible
class ContactFormModel(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.CharField(verbose_name="Sub-title", max_length=254)
    name_label = models.CharField(verbose_name="Label - name", max_length=254)
    email_label = models.CharField(verbose_name="Label - email", max_length=254)
    purpose_label = models.CharField(verbose_name="Label - purpose", max_length=254)
    text_label = models.CharField(verbose_name="Label - text", max_length=254)
    button_text = models.CharField(verbose_name="Button text", max_length=254)

    def copy_relations(self, old_instance):
        self.purpose_options.all().delete()

        for purpose_option in old_instance.purpose_options.all():
            purpose_option.pk = None
            purpose_option.parent = self
            purpose_option.save()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class ContactUs(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    button_text = models.CharField(verbose_name="Button text", max_length=254)
    link_text = models.CharField(verbose_name="Link text", max_length=254)
    link_external = models.URLField(
        verbose_name='External link',
        blank=True,
        max_length=2040,
        help_text='Provide a valid URL to an external website.',
    )
    link_internal = PageField(
        verbose_name='Internal link',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text='If provided, overrides the external link.',
    )

    @property
    def link_url(self):
        if self.link_internal:
            return self.link_internal.get_absolute_url()
        elif self.link_external:
            return self.link_external
        else:
            return ""

    def clean(self):
        super(ContactUs, self).clean()
        if not self.link_external and not self.link_internal:
            raise ValidationError("Please provide a link.")

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class ContactPerson(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.CharField(verbose_name="Sub-title", max_length=254, blank=True)
    person_name = models.CharField(verbose_name="Person name", max_length=254)
    person_title = models.CharField(verbose_name="Person title", max_length=254)
    person_phone = models.CharField(verbose_name="Person phone", max_length=254, blank=True)
    image = FilerImageField(verbose_name="Image", on_delete=models.PROTECT)
    button_text = models.CharField(verbose_name="Button text", max_length=254)
    button_link_external = models.URLField(
        verbose_name='Button external link',
        blank=True,
        max_length=2040,
        help_text='Provide a valid URL to an external website.',
    )
    button_link_internal = PageField(
        verbose_name='Button internal link',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text='If provided, overrides the external link.',
        related_name="contact_people_button"
    )
    more_text = models.CharField(verbose_name="More link text", max_length=254, blank=True)
    more_link_external = models.URLField(
        verbose_name='More external link',
        blank=True,
        max_length=2040,
        help_text='Provide a valid URL to an external website.',
    )
    more_link_internal = PageField(
        verbose_name='More internal link',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text='If provided, overrides the external link.',
        related_name="contact_people_more"
    )

    @property
    def button_link(self):
        if self.button_link_internal:
            return self.button_link_internal.get_absolute_url()
        elif self.button_link_external:
            return self.button_link_external
        else:
            return ""

    @property
    def more_link(self):
        if self.more_link_internal:
            return self.more_link_internal.get_absolute_url()
        elif self.more_link_external:
            return self.more_link_external
        else:
            return ""

    def clean(self):
        super(ContactPerson, self).clean()
        if not self.button_link_external and not self.button_link_internal:
            raise ValidationError("Please provide a link.")

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Map(CMSPlugin):
    title = models.TextField(verbose_name="Title")
    address = models.TextField(verbose_name="Address")
    ic = models.CharField(verbose_name="IČ with label", max_length=254)
    dic = models.CharField(verbose_name="DIČ with label", max_length=254)
    phone = models.CharField(verbose_name="Phone with label", max_length=254)
    email = models.CharField(verbose_name="Email with label", max_length=254)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class PositionSearch(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    search_placeholder = models.CharField(verbose_name="Search input placeholder", max_length=254)
    search_button = models.CharField(verbose_name="Search button text", max_length=254)
    all_pacts_text = models.CharField(verbose_name="All jobs text", max_length=254, default="Všechny úvazky")
    recruiter_text = models.CharField(verbose_name="Recruiter text", max_length=254, default="Provedu vás náborem")
    recruiter_email_text = models.CharField(verbose_name="Recruiter email text", max_length=254,
                                            default="Napište mi e-mail")
    more_button_text = models.CharField(verbose_name="More button text", max_length=254)
    limit = models.PositiveSmallIntegerField(verbose_name="Limit results", null=True, blank=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Quote(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.TextField(verbose_name="Sub-title")
    text = HTMLField(verbose_name="Text", configuration="CKEDITOR_SETTINGS_TEXT")
    author = models.CharField(verbose_name="Author", max_length=254)
    author_title = models.CharField(verbose_name="Author - title", max_length=254)
    author_image = FilerImageField(verbose_name="Author - image", on_delete=models.PROTECT)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class BubblePanel(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class BubbleCard(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    text = models.TextField(verbose_name="Text")
    bubble_highlight = models.CharField(verbose_name="Bubble highlight", max_length=254)
    bubble_text = models.CharField(verbose_name="Bubble text", max_length=254)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Timeline(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.TextField(verbose_name="Sub-title", blank=True)
    title_after = models.CharField(verbose_name="Title after", max_length=254, blank=True)
    subtitle_after = models.TextField(verbose_name="Sub-title after", blank=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class TimelineItem(CMSPlugin):
    image = FilerImageField(verbose_name="Image", on_delete=models.PROTECT, null=True, blank=True)
    text = models.TextField(verbose_name="Text", blank=True)

    def __str__(self):
        return self.text


@python_2_unicode_compatible
class AcaFriendPanel(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class AcaFriendCard(CMSPlugin):
    author = models.CharField(verbose_name="Author", max_length=254)
    author_position = models.CharField(verbose_name="Author position", max_length=254)
    image = FilerImageField(verbose_name="Image", on_delete=models.PROTECT)
    text = models.TextField(verbose_name="Text")

    def __str__(self):
        return self.author


@python_2_unicode_compatible
class GraphSection(CMSPlugin):
    button_text = models.CharField(verbose_name="Button text", max_length=254)
    button_link_external = models.URLField(
        verbose_name='Button external link',
        blank=True,
        max_length=2040,
        help_text='Provide a valid URL to an external website.',
    )
    button_link_internal = PageField(
        verbose_name='Button internal link',
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        help_text='If provided, overrides the external link.',
    )

    @property
    def link_url(self):
        if self.button_link_internal:
            return self.button_link_internal.get_absolute_url()
        elif self.button_link_external:
            return self.button_link_external
        else:
            return ""

    def clean(self):
        super(GraphSection, self).clean()
        if not self.button_link_external and not self.button_link_internal:
            raise ValidationError("Please provide a link.")

    def __str__(self):
        return self.button_text


@python_2_unicode_compatible
class GraphCard(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    image = FilerImageField(verbose_name="Image", on_delete=models.PROTECT)

    def copy_relations(self, old_instance):
        self.texts.all().delete()

        for text in old_instance.texts.all():
            text.pk = None
            text.parent = self
            text.save()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class GraphCardText(models.Model):
    parent = models.ForeignKey('acamar_web.GraphCard', related_name="texts", on_delete=models.CASCADE)
    text = models.CharField(verbose_name="Text", max_length=254)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Graph card text"
        verbose_name_plural = "Graph card texts"


@python_2_unicode_compatible
class PartnersModel(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.CharField(verbose_name="Sub-title", max_length=254)
    text = models.TextField(verbose_name="Text")

    def __str__(self):
        return self.title
