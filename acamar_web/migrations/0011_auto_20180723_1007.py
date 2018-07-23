# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0010_partnersmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='timeline',
            name='subtitle_after',
            field=models.TextField(verbose_name='Sub-title after', blank=True),
        ),
        migrations.AddField(
            model_name='timeline',
            name='title_after',
            field=models.CharField(max_length=254, verbose_name='Title after', blank=True),
        ),
        migrations.AlterField(
            model_name='timeline',
            name='subtitle',
            field=models.TextField(verbose_name='Sub-title', blank=True),
        ),
    ]
