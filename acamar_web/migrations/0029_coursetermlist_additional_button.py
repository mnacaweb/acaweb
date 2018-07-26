# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0028_auto_20180726_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursetermlist',
            name='additional_button',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Additional registration - button', blank=True, to='acamar_web.Link', null=True),
        ),
    ]
