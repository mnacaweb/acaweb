# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PositionCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254, verbose_name=b'Name')),
                ('name_cs', models.CharField(max_length=254, null=True, verbose_name=b'Name')),
                ('name_en', models.CharField(max_length=254, null=True, verbose_name=b'Name')),
                ('name_ru', models.CharField(max_length=254, null=True, verbose_name=b'Name')),
            ],
            options={
                'verbose_name': 'Position category',
                'verbose_name_plural': 'Position categories',
            },
        ),
    ]
