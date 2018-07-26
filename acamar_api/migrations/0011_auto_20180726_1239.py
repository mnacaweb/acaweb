# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_api', '0010_auto_20180726_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.SlugField(verbose_name='Url-slug'),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug_cs',
            field=models.SlugField(null=True, verbose_name='Url-slug'),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug_en',
            field=models.SlugField(null=True, verbose_name='Url-slug'),
        ),
        migrations.AlterField(
            model_name='course',
            name='slug_ru',
            field=models.SlugField(null=True, verbose_name='Url-slug'),
        ),
    ]
