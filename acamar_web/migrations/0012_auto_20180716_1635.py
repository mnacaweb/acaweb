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
        ('acamar_web', '0011_auto_20180716_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_logo', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('image', filer.fields.image.FilerImageField(related_name='teamwork_logos', on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='LogoPanel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_logopanel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('button_text', models.CharField(max_length=254, verbose_name='Button text')),
                ('button_link', cms.models.fields.PageField(verbose_name='Button link', to='cms.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.DeleteModel(
            name='Teamwork',
        ),
        migrations.DeleteModel(
            name='TeamworkLogo',
        ),
    ]
