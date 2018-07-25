# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_api', '0003_course'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
        migrations.AddField(
            model_name='course',
            name='meta_keywords',
            field=models.CharField(max_length=254, null=True, verbose_name=b'Meta keywords'),
        ),
        migrations.AddField(
            model_name='course',
            name='slug_cs',
            field=models.SlugField(unique=True, null=True, verbose_name=b'Url-slug'),
        ),
        migrations.AddField(
            model_name='course',
            name='slug_en',
            field=models.SlugField(unique=True, null=True, verbose_name=b'Url-slug'),
        ),
        migrations.AddField(
            model_name='course',
            name='slug_ru',
            field=models.SlugField(unique=True, null=True, verbose_name=b'Url-slug'),
        ),
    ]
