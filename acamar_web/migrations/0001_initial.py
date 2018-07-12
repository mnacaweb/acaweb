# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
from django.conf import settings
import acamar_web.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0010_auto_20180414_2058'),
        ('cms', '0020_old_tree_cleanup'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerVideo',
            fields=[
                ('file_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='filer.File')),
            ],
            options={
                'abstract': False,
            },
            bases=('filer.file',),
        ),
        migrations.CreateModel(
            name='MainBanner',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_mainbanner', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default='default', max_length=100, verbose_name='Template', choices=[('default', 'Default'), ('candidates', 'Candidates'), ('we_are', 'We are'), ('course', 'Course'), ('contact', 'Contact'), ('detail', 'Detail')])),
                ('title', models.TextField(verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Sub-title')),
                ('background_image', filer.fields.image.FilerImageField(blank=True, to=settings.FILER_IMAGE_MODEL, help_text='Fallback for background video', null=True, verbose_name='Background image')),
                ('background_video', acamar_web.fields.FilerVideoField(verbose_name='Background video', blank=True, to='acamar_web.FilerVideo', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
