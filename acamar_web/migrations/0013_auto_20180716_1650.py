# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0012_auto_20180716_1635'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teammember',
            options={'ordering': ['order'], 'verbose_name': 'Team member', 'verbose_name_plural': 'Team members'},
        ),
        migrations.AddField(
            model_name='teammember',
            name='order',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
        ),
    ]
