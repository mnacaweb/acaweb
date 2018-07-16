# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings
import filer.fields.image
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('acamar_web', '0007_review_show'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teamwork',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_teamwork', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('button_text', models.CharField(max_length=254, verbose_name='Button text')),
                ('button_link', cms.models.fields.PageField(verbose_name='Button link', to='cms.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TeamworkLogo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_teamworklogo', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('image', filer.fields.image.FilerImageField(related_name='teamwork_logos', on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
