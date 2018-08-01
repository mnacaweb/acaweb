# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from urlparse import urljoin

from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save, m2m_changed
from django.dispatch import receiver

from .models import PositionApply, CourseEnroll


@receiver(post_save, sender=PositionApply, dispatch_uid="position_apply_email")
def position_apply_email(instance, created, **kwargs):
    if created:
        domain = Site.objects.get_current().domain
        mail = EmailMessage(
            subject="Nový uchazeč - {}".format(instance.position.name),
            body="Odkaz do adminu: {}\n"
                 "\n"
                 "Pozice: {}\n"
                 "Jméno: {}\n"
                 "Příjmení: {}\n"
                 "E-mail: {}\n"
                 "Telefon: {}\n"
                 "CV: {}\n"
                 "LinkedIn: {}\n"
                 "Text: {}".format(
                urljoin(domain, reverse("admin:acamar_api_positionapply_change",
                                        args=(instance.id,))), instance.position.name, instance.first_name,
                instance.last_name,
                instance.email, instance.phone, urljoin(domain, instance.cv.url) if instance.cv else "--",
                instance.linkedin,
                instance.text),
            to=[instance.position_user_email]
        )
        mail.send()


@receiver(m2m_changed, sender=CourseEnroll.courses.through, dispatch_uid="course_enroll_email")
def course_enroll_email(instance, action, **kwargs):
    if action == "post_add":
        domain = Site.objects.get_current().domain
        mail = EmailMessage(
            subject="Nová přihláška ke kurzům",
            body="Odkaz do adminu: {}\n"
                 "\n"
                 "Jméno: {}\n"
                 "Telefon: {}\n"
                 "Kurzy: {}\n"
                 "CV: {}\n"
                 "Očekávání: {}".format(
                urljoin(domain, reverse("admin:acamar_api_courseenroll_change", args=(instance.id,))), instance.name,
                instance.phone, instance.course_terms, urljoin(domain, instance.cv.url) if instance.cv else "--",
                instance.expectations),
            to=["lucie.stankova@acamar.cz"]
        )
        mail.send()


def _():
    pass
