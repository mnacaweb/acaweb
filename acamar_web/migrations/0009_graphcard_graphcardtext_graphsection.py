# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import cms.models.fields
import filer.fields.image
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('acamar_web', '0008_auto_20180720_1431'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphCard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_graphcard', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='GraphCardText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=254, verbose_name='Text')),
                ('parent', models.ForeignKey(related_name='texts', to='acamar_web.GraphCard')),
            ],
            options={
                'verbose_name': 'Graph card text',
                'verbose_name_plural': 'Graph card texts',
            },
        ),
        migrations.CreateModel(
            name='GraphSection',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_graphsection', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('button_text', models.CharField(max_length=254, verbose_name='Button text')),
                ('button_link_external', models.URLField(help_text='Provide a valid URL to an external website.', max_length=2040, verbose_name='Button external link', blank=True)),
                ('button_link_internal', cms.models.fields.PageField(blank=True, to='cms.Page', help_text='If provided, overrides the external link.', null=True, verbose_name='Button internal link')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
