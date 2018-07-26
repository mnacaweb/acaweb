# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_api', '0009_auto_20180725_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseterm',
            name='course',
            field=models.ForeignKey(related_name='terms', verbose_name=b'Course', to='acamar_api.Course'),
        ),
    ]
