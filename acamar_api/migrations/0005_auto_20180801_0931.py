# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_api', '0004_auto_20180731_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='meta_description',
            field=models.CharField(max_length=254, verbose_name='Meta description', blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_description_cs',
            field=models.CharField(max_length=254, null=True, verbose_name='Meta description', blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_description_en',
            field=models.CharField(max_length=254, null=True, verbose_name='Meta description', blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_description_ru',
            field=models.CharField(max_length=254, null=True, verbose_name='Meta description', blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_title',
            field=models.CharField(max_length=254, verbose_name='Meta title', blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_title_cs',
            field=models.CharField(max_length=254, null=True, verbose_name='Meta title', blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_title_en',
            field=models.CharField(max_length=254, null=True, verbose_name='Meta title', blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_title_ru',
            field=models.CharField(max_length=254, null=True, verbose_name='Meta title', blank=True),
        ),
    ]
