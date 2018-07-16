# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0010_createteam_createteamcard'),
    ]

    operations = [
        migrations.CreateModel(
            name='TeamGrid',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_teamgrid', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Sub-title')),
                ('button_text', models.CharField(max_length=254, verbose_name='Button text')),
                ('limit', models.PositiveSmallIntegerField(null=True, verbose_name='Limit count', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254, verbose_name='Name')),
                ('nickname', models.CharField(max_length=254, verbose_name='Position / Nickname')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Team member',
                'verbose_name_plural': 'Team members',
            },
        ),
        migrations.AlterField(
            model_name='createteam',
            name='subtitle',
            field=models.TextField(verbose_name='Sub-title'),
        ),
    ]
