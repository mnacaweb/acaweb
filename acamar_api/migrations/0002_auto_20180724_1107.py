# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_api', '0001_squashed'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='slug',
            field=models.SlugField(max_length=120, blank=True),
        ),
        migrations.AddField(
            model_name='position',
            name='slug_cs',
            field=models.SlugField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='position',
            name='slug_en',
            field=models.SlugField(max_length=120, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='position',
            name='slug_ru',
            field=models.SlugField(max_length=120, null=True, blank=True),
        ),
    ]
