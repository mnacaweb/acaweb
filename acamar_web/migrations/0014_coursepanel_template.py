# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0013_auto_20180723_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursepanel',
            name='template',
            field=models.CharField(default='', max_length=20, verbose_name='Template', blank=True, choices=[('', 'Default'), ('_alternative', 'Alternative with background')]),
        ),
    ]
