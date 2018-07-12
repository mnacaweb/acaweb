# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainBannerCard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_mainbannercard', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.TextField(verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Sub-title')),
                ('button_text', models.CharField(max_length=254, verbose_name='Button text')),
                ('theme', models.CharField(blank=True, max_length=30, verbose_name='Theme', choices=[('', 'Black'), ('looking-for-gray', 'Gray')])),
                ('button_link', cms.models.fields.PageField(verbose_name='Button link', to='cms.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
