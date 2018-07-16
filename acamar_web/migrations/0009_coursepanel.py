# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0008_teamwork_teamworklogo'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePanel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_coursepanel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=254, verbose_name='Sub-title')),
                ('text', models.TextField(verbose_name='Text')),
                ('button_text', models.CharField(max_length=254, verbose_name='Button text')),
                ('button_link', cms.models.fields.PageField(verbose_name='Button link', to='cms.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
