# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0006_auto_20180713_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='show',
            field=models.BooleanField(default=True, db_index=True, verbose_name='Show'),
        ),
    ]
