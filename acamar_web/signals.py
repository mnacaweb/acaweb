# -*- coding: utf-8 -*-


from urllib.parse import urljoin

from django.contrib.sites.models import Site
from django.core.mail import EmailMessage
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

from acamar_web.models import Contact


@receiver(post_save, sender=Contact, dispatch_uid="contact_email")
def contact_email(instance, created, **kwargs):
    if created:
        domain = Site.objects.get_current().domain
        mail = EmailMessage(
            subject="New message - {}".format(instance.name),
            body="Odkaz do adminu: {}\n"
            "\n"
            "Jméno: {}\n"
            "E-mail: {}\n"
            "Téma: {}\n"
            "Text: {}\n".format(
                urljoin(
                    domain,
                    reverse("admin:acamar_web_contact_change", args=(instance.id,)),
                ),
                instance.name,
                instance.email,
                instance.purpose,
                instance.text,
            ),
            to=["info@acamar.cz"],
        )
        mail.send()


def _():
    pass
