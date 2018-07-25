# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_api', '0006_courseterm'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTermItem',
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
            ],
            options={
                'verbose_name': 'Course term - item',
                'verbose_name_plural': 'Course term - items',
            },
        ),
        migrations.AlterModelOptions(
            name='courseterm',
            options={'verbose_name': 'Course term', 'verbose_name_plural': 'Course terms'},
        ),
        migrations.RemoveField(
            model_name='courseterm',
            name='address',
        ),
        migrations.RemoveField(
            model_name='courseterm',
            name='address_cs',
        ),
        migrations.RemoveField(
            model_name='courseterm',
            name='address_en',
        ),
        migrations.RemoveField(
            model_name='courseterm',
            name='address_ru',
        ),
        migrations.RemoveField(
            model_name='courseterm',
            name='date',
        ),
        migrations.RemoveField(
            model_name='courseterm',
            name='description',
        ),
        migrations.RemoveField(
            model_name='courseterm',
            name='description_cs',
        ),
        migrations.RemoveField(
            model_name='courseterm',
            name='description_en',
        ),
        migrations.RemoveField(
            model_name='courseterm',
            name='description_ru',
        ),
        migrations.RemoveField(
            model_name='courseterm',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='courseterm',
            name='start_time',
        ),
    ]
