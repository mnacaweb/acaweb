# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0021_auto_20180725_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseBonusCard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_coursebonuscard', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('text', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CourseBonusPanel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_coursebonuspanel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='createteam',
            name='subtitle',
            field=models.TextField(verbose_name='Sub-title', blank=True),
        ),
        migrations.AlterField(
            model_name='createteamcard',
            name='subtitle',
            field=models.CharField(max_length=254, verbose_name='Sub-title', blank=True),
        ),
    ]
