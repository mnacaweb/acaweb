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
        ('acamar_web', '0014_teammember_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactCard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_contactcard', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=254, verbose_name='Name')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email', blank=True)),
                ('linkedin', models.URLField(verbose_name='LinedIn URL', blank=True)),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ContactGrid',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_contactgrid', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
