# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_api', '0005_auto_20180725_1225'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTerm',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name=b'Date')),
                ('start_time', models.TimeField(verbose_name=b'Start time')),
                ('end_time', models.TimeField(null=True, verbose_name=b'End time', blank=True)),
                ('address', models.CharField(max_length=254, verbose_name=b'Address', blank=True)),
                ('address_cs', models.CharField(max_length=254, null=True, verbose_name=b'Address', blank=True)),
                ('address_en', models.CharField(max_length=254, null=True, verbose_name=b'Address', blank=True)),
                ('address_ru', models.CharField(max_length=254, null=True, verbose_name=b'Address', blank=True)),
                ('description', models.CharField(max_length=254, verbose_name=b'Description', blank=True)),
                ('description_cs', models.CharField(max_length=254, null=True, verbose_name=b'Description', blank=True)),
                ('description_en', models.CharField(max_length=254, null=True, verbose_name=b'Description', blank=True)),
                ('description_ru', models.CharField(max_length=254, null=True, verbose_name=b'Description', blank=True)),
                ('course', models.ForeignKey(verbose_name=b'Course', to='acamar_api.Course')),
            ],
            options={
                'verbose_name': 'Course term',
            },
        ),
    ]
