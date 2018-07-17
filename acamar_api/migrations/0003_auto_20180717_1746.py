# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_api', '0002_auto_20180717_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='lang',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='position',
            name='lang_cs',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='position',
            name='lang_en',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='position',
            name='lang_ru',
            field=models.BooleanField(default=False),
        ),
    ]
