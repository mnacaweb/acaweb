# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0016_auto_20180717_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='nickname_cs',
            field=models.CharField(max_length=254, null=True, verbose_name='Position / Nickname'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='nickname_en',
            field=models.CharField(max_length=254, null=True, verbose_name='Position / Nickname'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='nickname_ru',
            field=models.CharField(max_length=254, null=True, verbose_name='Position / Nickname'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='text_cs',
            field=models.TextField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Text'),
        ),
    ]
