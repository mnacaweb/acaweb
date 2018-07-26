# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_api', '0012_course_main_banner_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='main_banner_title_cs',
            field=models.CharField(max_length=254, null=True, verbose_name='Main banner title'),
        ),
        migrations.AddField(
            model_name='course',
            name='main_banner_title_en',
            field=models.CharField(max_length=254, null=True, verbose_name='Main banner title'),
        ),
        migrations.AddField(
            model_name='course',
            name='main_banner_title_ru',
            field=models.CharField(max_length=254, null=True, verbose_name='Main banner title'),
        ),
    ]
