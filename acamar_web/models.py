# coding: utf-8

from __future__ import unicode_literals

import base64
import os
import urllib
from random import shuffle

from adminsortable.models import SortableMixin
from cms.models import CMSPlugin
from cms.models.fields import PageField
from django.conf import settings
from django.contrib.sites.models import Site
from django.core.exceptions import ValidationError
from django.db import models
from django.template.defaultfilters import truncatechars
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible, force_text
from django.utils.functional import cached_property
from django.utils.translation import get_language
from djangocms_text_ckeditor.fields import HTMLField
from filer.fields.image import FilerImageField
from filer.models import File

from acamar_api.models import Course


class FilerVideo(File):
    _icon = "video"

    @classmethod
    def matches_file_type(cls, name, file, request):
        # the extensions we'll recognise for this file type
        filename_extensions = ['.mp4', '.webm', '.ogg']
        ext = os.path.splitext(name)[1].lower()
        return ext in filename_extensions


@python_2_unicode_compatible
class Link(models.Model):
    TARGET_CHOICES = (
        ('_blank', 'Open in new window'),
        ('_self', 'Open in same window'),
        ('_parent', 'Delegate to parent'),
        ('_top', 'Delegate to top'),
    )
    text = models.CharField(verbose_name='Link text', max_length=255)
    external_link = models.URLField(verbose_name='External link', blank=True, max_length=2040,
                                    help_text='Provide a valid URL to an external website.')
    internal_link = PageField(verbose_name='Internal link', blank=True, null=True, on_delete=models.SET_NULL,
                              help_text='If provided, overrides the external link.')
    mailto = models.EmailField(verbose_name='Email address', blank=True, max_length=255)
    phone = models.CharField(verbose_name='Phone', blank=True, max_length=255)
    target = models.CharField(verbose_name='Target', choices=TARGET_CHOICES, blank=True, max_length=255)
    anchor = models.CharField(verbose_name='Anchor', blank=True, max_length=255,
                              help_text='Appends the value only after the internal or external link. '
                                        'Do <em>not</em> include a preceding "#" symbol.')

    def __str__(self):
        return "{} - {}".format(self.text, self.get_link)

    @cached_property
    def mailto_safe(self):
        mail = self.mailto.split("@")
        return "aca{}mar@{}".format(base64.b64encode(mail[0]), mail[1])

    @cached_property
    def get_link(self):
        if self.internal_link:
            link = self.internal_link.get_absolute_url()
        elif self.external_link:
            link = self.external_link
        elif self.phone:
            link = 'tel:{}'.format(self.phone.replace(' ', ''))
        elif self.mailto:
            link = 'mailto:{}'.format(self.mailto)
        else:
            link = ''

        if (not self.phone and not self.mailto) and self.anchor:
            link += '#{}'.format(self.anchor)

        return link

    @cached_property
    def get_link_safe(self):
        if self.internal_link:
            link = self.internal_link.get_absolute_url()
        elif self.external_link:
            link = self.external_link
        elif self.phone:
            link = 'tel:{}'.format(self.phone.replace(' ', ''))
        elif self.mailto:
            link = 'mailto:{}'.format(self.mailto_safe)
        else:
            link = ''

        if (not self.phone and not self.mailto) and self.anchor:
            link += '#{}'.format(self.anchor)

        return link

    def clean(self):
        super(Link, self).clean()
        field_names = (
            'external_link',
            'internal_link',
            'mailto',
            'phone',
        )

        link_fields = {
            key: getattr(self, key)
            for key in field_names
        }
        link_field_verbose_names = {
            key: force_text(self._meta.get_field(key).verbose_name)
            for key in link_fields.keys()
        }
        provided_link_fields = {
            key: value
            for key, value in link_fields.items()
            if value
        }

        if len(provided_link_fields) > 1:
            verbose_names = sorted(link_field_verbose_names.values())
            error_msg = 'Only one of {0} or {1} may be given.'.format(
                ', '.join(verbose_names[:-1]),
                verbose_names[-1],
            )
            errors = {}.fromkeys(provided_link_fields.keys(), error_msg)
            raise ValidationError(errors)

        if len(provided_link_fields) == 0 and not self.anchor:
            raise ValidationError('Please provide a link.')


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
    AKARTA = "a-card"
    ENROLL_IN_COURSE = "enroll_in_course"
    _CHOICES = [
        (DEFAULT, "Default"),
        (FOR_CANDIDATES, "For candidates"),
        (FOR_COMPANIES, "For companies"),
        (WE_ARE, "We are"),
        (COURSE, "Course"),
        (CONTACT, "Contact"),
        (DETAIL, "Detail"),
        (AKARTA, "A-card"),
        (ENROLL_IN_COURSE, "Enroll in course")
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
    button = models.ForeignKey("acamar_web.Link", on_delete=models.PROTECT, verbose_name="Button", blank=True,
                               null=True)
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
    button = models.ForeignKey("acamar_web.Link", on_delete=models.PROTECT, verbose_name="Button", blank=True,
                               null=True)

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
    subtitle = models.CharField(verbose_name="Sub-title", max_length=254, blank=True)
    template = models.CharField(verbose_name="Template", max_length=20, choices=_TEMPLATE_OPTIONS, blank=True,
                                default=DEFAULT)
    text = models.TextField(verbose_name="Text", blank=True)
    button = models.ForeignKey("acamar_web.Link", on_delete=models.PROTECT, verbose_name="Button", blank=True,
                               null=True)

    def __str__(self):
        return self.title

    def courses(self):
        items = Course.objects.filter(coursepanelitem__course_panel=self)
        if items.exists():
            return items
        return Course.objects.all()

    def copy_relations(self, old_instance):
        self.items.all().delete()

        for item in old_instance.items.all():
            item.pk = None
            item.course_panel = self
            item.save()


@python_2_unicode_compatible
class CoursePanelItem(models.Model):
    course_panel = models.ForeignKey("acamar_web.CoursePanel", on_delete=models.CASCADE, related_name="items")
    course = models.ForeignKey("acamar_api.Course", verbose_name="Course", on_delete=models.PROTECT)

    def __str__(self):
        return self.course.title

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"


@python_2_unicode_compatible
class CreateTeam(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.TextField(verbose_name="Sub-title", blank=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class CreateTeamCard(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.CharField(verbose_name="Sub-title", max_length=254, blank=True)
    image = FilerImageField(verbose_name="Image", on_delete=models.PROTECT)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class TeamGrid(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.TextField(verbose_name="Sub-title")
    button_text = models.CharField(verbose_name="Button text", max_length=254)
    more_button = models.ForeignKey("acamar_web.Link", on_delete=models.PROTECT, verbose_name="More button",
                                    blank=True, null=True)
    limit = models.PositiveSmallIntegerField(verbose_name="Limit count", null=True, blank=True)

    @cached_property
    def members(self):
        member_list = list(TeamMember.objects.all())
        shuffle(member_list)
        return member_list

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
    success_text = models.CharField(verbose_name="Success text", max_length=254)

    def copy_relations(self, old_instance):
        self.purpose_options.all().delete()

        for purpose_option in old_instance.purpose_options.all():
            purpose_option.pk = None
            purpose_option.form = self
            purpose_option.save()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class ContactUs(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    button = models.ForeignKey("acamar_web.Link", on_delete=models.PROTECT, verbose_name="Button", blank=True,
                               null=True, related_name="contact_us_button_set")
    additional_link = models.ForeignKey("acamar_web.Link", on_delete=models.PROTECT, verbose_name="Additional link",
                                        blank=True, null=True, related_name="contact_us_additional_set")

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
    button = models.ForeignKey("acamar_web.Link", on_delete=models.PROTECT, verbose_name="Button", blank=True,
                               null=True, related_name="contact_person_button_set")
    more = models.ForeignKey("acamar_web.Link", on_delete=models.PROTECT, verbose_name="More link", blank=True,
                             null=True, related_name="contact_person_more_set")

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
    title = models.CharField(verbose_name="Title", blank=True, max_length=254)
    text = models.TextField(verbose_name="Text", blank=True)

    def __str__(self):
        return self.title if self.title else self.text


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
    button = models.ForeignKey("acamar_web.Link", on_delete=models.PROTECT, verbose_name="Button", blank=True,
                               null=True)

    def __str__(self):
        return self.button.text if self.button else ""


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

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class PartnersItem(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    text = HTMLField(verbose_name="Text", configuration="CKEDITOR_SETTINGS_TEXT")
    image = FilerImageField(verbose_name="Image", on_delete=models.PROTECT)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class CourseLector(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    person_name = models.CharField(verbose_name="Person name", max_length=254)
    person_title = models.CharField(verbose_name="Person title", max_length=254)
    person_image = FilerImageField(verbose_name="Person image", on_delete=models.PROTECT)
    text = HTMLField(verbose_name="Text", configuration="CKEDITOR_SETTINGS_TEXT")

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class AcardBenefits(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.CharField(verbose_name="Sub-title", max_length=254)
    text = HTMLField(verbose_name="Text", configuration="CKEDITOR_SETTINGS_TEXT")

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class AcardBenefitsItem(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    icon = FilerImageField(verbose_name="Icon", on_delete=models.PROTECT)
    subtitle = models.TextField(verbose_name="Subtitle")
    text = HTMLField(verbose_name="Text", configuration="CKEDITOR_SETTINGS_TEXT")

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class CourseBonusPanel(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class CourseBonusCard(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    text = HTMLField(verbose_name="Text", configuration="CKEDITOR_SETTINGS_TEXT")

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class CourseProgram(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.CharField(verbose_name="Sub-title", max_length=254, blank=True)

    def copy_relations(self, old_instance):
        self.items.all().delete()

        for item in old_instance.items.all():
            item.pk = None
            item.parent = self
            item.save()

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class CourseProgramItem(models.Model):
    parent = models.ForeignKey("acamar_web.CourseProgram", on_delete=models.CASCADE, related_name="items")
    text = models.CharField(verbose_name="Text", max_length=254)

    def __str__(self):
        return self.text


@python_2_unicode_compatible
class CourseTermList(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.CharField(verbose_name="Sub-title", max_length=254, blank=True)
    button = models.ForeignKey("acamar_web.Link", on_delete=models.PROTECT, verbose_name="Registration button")
    additional_registration = models.BooleanField(verbose_name="Additional registration", default=False)
    additional_title = models.CharField(verbose_name="Additional registration - title", max_length=254, blank=True)

    def __str__(self):
        return self.title

    def clean(self):
        super(CourseTermList, self).clean()
        if self.additional_registration and (not self.additional_title):
            raise ValidationError("Provide Additional registration - title")

    def copy_relations(self, old_instance):
        self.additional_items.all().delete()

        for item in old_instance.additional_items.all():
            item.pk = None
            item.parent = self
            item.save()


@python_2_unicode_compatible
class CourseTermListAdditional(models.Model):
    parent = models.ForeignKey("acamar_web.CourseTermList", on_delete=models.CASCADE, related_name="additional_items")
    address = models.CharField(verbose_name="Address", max_length=254, blank=True)
    description = models.CharField(verbose_name="Description", max_length=254, blank=True)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Additional registration - item"
        verbose_name_plural = "Additional registration - items"


@python_2_unicode_compatible
class CourseGenericRegistration(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    text = HTMLField(verbose_name="Text", configuration="CKEDITOR_SETTINGS_TEXT")
    button = models.ForeignKey("acamar_web.Link", on_delete=models.PROTECT, verbose_name="Button")

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class CourseBasicInfo(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class CourseBasicInfoCard(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    image = FilerImageField(verbose_name="Image", on_delete=models.PROTECT)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class CourseEnrollFormModel(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    name_label = models.CharField(verbose_name="Name label", max_length=254)
    phone_label = models.CharField(verbose_name="Phone label", max_length=254)
    email_label = models.CharField(verbose_name="Email label", max_length=254)
    course_label = models.CharField(verbose_name="Course select label", max_length=254)
    expectations_label = models.CharField(verbose_name="Expectations label", max_length=254)
    cv_label = models.CharField(verbose_name="CV label", max_length=254)
    cv_picker_label = models.CharField(verbose_name="CV - choose file label", max_length=254)
    submit_text = models.CharField(verbose_name="Submit button text", max_length=254)
    selected_text = models.CharField(verbose_name="Multi-select selected text", max_length=30, default="vybráno")
    thanks_page = PageField(verbose_name="Thanks page", on_delete=models.PROTECT)

    def __str__(self):
        return self.title

    def get_courses(self):
        return Course.objects.prefetch_related("terms", "terms__items").exclude(terms__items__date__lt=timezone.now())


@python_2_unicode_compatible
class LoginPluginModel(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    subtitle = models.CharField(verbose_name="Sub-title", max_length=254, blank=True)
    username_label = models.CharField(verbose_name="Username label", max_length=254)
    password_label = models.CharField(verbose_name="Password label", max_length=254)
    button_text = models.CharField(verbose_name="Button text", max_length=254)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class Contact(models.Model):
    name = models.CharField(verbose_name="Name", max_length=254)
    email = models.EmailField(verbose_name="Email", max_length=254)
    purpose = models.CharField(verbose_name="Purpose", max_length=254)
    text = models.TextField(verbose_name="Text", blank=True)
    language = models.CharField(verbose_name="Language", max_length=3, choices=settings.LANGUAGES, default=get_language)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Contact"
        verbose_name_plural = "Contacts"


@python_2_unicode_compatible
class ThanksBanner(CMSPlugin):
    title = models.CharField(verbose_name="Title", max_length=254)
    text = HTMLField(verbose_name="Text", configuration="CKEDITOR_SETTINGS_TEXT")

    def __str__(self):
        return self.title
