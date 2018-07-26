# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0023_courseprogram_courseprogramitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTermList',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_coursetermlist', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=254, verbose_name='Sub-title', blank=True)),
                ('additional_registration', models.BooleanField(default=True, verbose_name='Additional registration')),
                ('additional_title', models.CharField(max_length=254, verbose_name='Additional registration - title', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='coursepanel',
            name='subtitle',
            field=models.CharField(max_length=254, verbose_name='Sub-title', blank=True),
        ),
        migrations.AlterField(
            model_name='coursepanel',
            name='text',
            field=models.TextField(verbose_name='Text', blank=True),
        ),
    ]
