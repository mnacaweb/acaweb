# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ["name", "email", "purpose", "text"]