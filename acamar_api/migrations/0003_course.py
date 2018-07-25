# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_api', '0002_auto_20180724_1107'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=254, verbose_name=b'Title')),
                ('title_cs', models.CharField(max_length=254, null=True, verbose_name=b'Title')),
                ('title_en', models.CharField(max_length=254, null=True, verbose_name=b'Title')),
                ('title_ru', models.CharField(max_length=254, null=True, verbose_name=b'Title')),
                ('slug', models.SlugField(unique=True, verbose_name=b'Url-slug')),
                ('short_description', models.TextField(verbose_name=b'Short description')),
                ('short_description_cs', models.TextField(null=True, verbose_name=b'Short description')),
                ('short_description_en', models.TextField(null=True, verbose_name=b'Short description')),
                ('short_description_ru', models.TextField(null=True, verbose_name=b'Short description')),
                ('place', models.CharField(max_length=254, verbose_name=b'Place', blank=True)),
                ('place_cs', models.CharField(max_length=254, null=True, verbose_name=b'Place', blank=True)),
                ('place_en', models.CharField(max_length=254, null=True, verbose_name=b'Place', blank=True)),
                ('place_ru', models.CharField(max_length=254, null=True, verbose_name=b'Place', blank=True)),
                ('price', models.PositiveIntegerField(null=True, verbose_name=b'Price', blank=True)),
                ('price_cs', models.PositiveIntegerField(null=True, verbose_name=b'Price', blank=True)),
                ('price_en', models.PositiveIntegerField(null=True, verbose_name=b'Price', blank=True)),
                ('price_ru', models.PositiveIntegerField(null=True, verbose_name=b'Price', blank=True)),
                ('duration', models.CharField(max_length=254, verbose_name=b'Duration', blank=True)),
                ('duration_cs', models.CharField(max_length=254, null=True, verbose_name=b'Duration', blank=True)),
                ('duration_en', models.CharField(max_length=254, null=True, verbose_name=b'Duration', blank=True)),
                ('duration_ru', models.CharField(max_length=254, null=True, verbose_name=b'Duration', blank=True)),
                ('content', cms.models.fields.PlaceholderField(slotname=b'course_content', editable=False, to='cms.Placeholder', null=True)),
            ],
        ),
    ]
