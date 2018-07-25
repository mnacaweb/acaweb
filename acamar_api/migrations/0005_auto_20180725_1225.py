# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_api', '0004_auto_20180725_1217'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='meta_keywords_cs',
            field=models.CharField(max_length=254, null=True, verbose_name=b'Meta keywords', blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_keywords_en',
            field=models.CharField(max_length=254, null=True, verbose_name=b'Meta keywords', blank=True),
        ),
        migrations.AddField(
            model_name='course',
            name='meta_keywords_ru',
            field=models.CharField(max_length=254, null=True, verbose_name=b'Meta keywords', blank=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='meta_keywords',
            field=models.CharField(default='', max_length=254, verbose_name=b'Meta keywords', blank=True),
            preserve_default=False,
        ),
    ]
