# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0022_positionsearch'),
    ]

    operations = [
        migrations.AddField(
            model_name='positionsearch',
            name='limit',
            field=models.PositiveSmallIntegerField(null=True, verbose_name='Limit results', blank=True),
        ),
    ]
