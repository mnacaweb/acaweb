# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('acamar_web', '0003_bubblecard_bubblepanel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_timeline', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Sub-title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TimelineItem',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_timelineitem', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('text', models.TextField(verbose_name='Text', blank=True)),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', blank=True, to=settings.FILER_IMAGE_MODEL, null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
