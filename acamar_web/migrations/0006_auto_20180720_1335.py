# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0005_acafriendcard_acafriendpanel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='acafriendcard',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
    ]
