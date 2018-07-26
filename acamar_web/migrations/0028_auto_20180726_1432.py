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
        ('acamar_web', '0027_remove_link_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseBasicInfo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_coursebasicinfo', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CourseBasicInfoCard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_coursebasicinfocard', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='courseprogram',
            name='subtitle',
            field=models.CharField(max_length=254, verbose_name='Sub-title', blank=True),
        ),
    ]
