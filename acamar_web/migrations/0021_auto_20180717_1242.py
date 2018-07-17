# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0020_auto_20180717_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='map',
            name='title',
            field=models.TextField(verbose_name='Title'),
        ),
    ]
