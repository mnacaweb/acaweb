# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0007_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainbanner',
            name='template',
            field=models.CharField(default='default', max_length=100, verbose_name='Template', choices=[('default', 'Default'), ('for_candidates', 'For candidates'), ('for_companies', 'For companies'), ('we_are', 'We are'), ('course', 'Course'), ('contact', 'Contact'), ('detail', 'Detail')]),
        ),
    ]
