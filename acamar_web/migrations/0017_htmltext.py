# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0016_auto_20190625_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='HtmlText',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_htmltext', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('text', models.TextField(verbose_name='Text', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
