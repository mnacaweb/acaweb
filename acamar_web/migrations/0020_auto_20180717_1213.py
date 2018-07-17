# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0019_contactformpurposeoption'),
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_map', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('address', models.TextField(verbose_name='Address')),
                ('ic', models.CharField(max_length=254, verbose_name='I\u010c with label')),
                ('dic', models.CharField(max_length=254, verbose_name='DI\u010c with label')),
                ('phone', models.CharField(max_length=254, verbose_name='Phone with label')),
                ('email', models.CharField(max_length=254, verbose_name='Email with label')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterModelOptions(
            name='contactformpurposeoption',
            options={'verbose_name': 'Purpose option', 'verbose_name_plural': 'Purpose options'},
        ),
    ]
