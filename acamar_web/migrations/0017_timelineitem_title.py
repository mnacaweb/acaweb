# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0016_courselector'),
    ]

    operations = [
        migrations.AddField(
            model_name='timelineitem',
            name='title',
            field=models.CharField(max_length=254, verbose_name='Title', blank=True),
        ),
    ]
