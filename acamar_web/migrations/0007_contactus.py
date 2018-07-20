# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0006_auto_20180720_1335'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_contactus', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('button_text', models.CharField(max_length=254, verbose_name='Button text')),
                ('link_text', models.CharField(max_length=254, verbose_name='Link text')),
                ('link_external', models.URLField(help_text='Provide a valid URL to an external website.', max_length=2040, verbose_name='External link', blank=True)),
                ('link_internal', cms.models.fields.PageField(blank=True, to='cms.Page', help_text='If provided, overrides the external link.', null=True, verbose_name='Internal link')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
