# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0026_auto_20180726_1154'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='link',
            name='name',
        ),
    ]