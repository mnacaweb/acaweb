# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0004_auto_20180713_1032'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewPanel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_reviewpanel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Sub-title')),
                ('positions_pretext', models.CharField(max_length=254, verbose_name='Positions - pre-text')),
                ('positions_number', models.PositiveSmallIntegerField(verbose_name='Positions - number')),
                ('positions_posttext', models.CharField(max_length=254, verbose_name='Positions - post-text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
