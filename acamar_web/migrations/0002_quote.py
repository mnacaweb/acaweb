# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion
import djangocms_text_ckeditor.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('acamar_web', '0001_squashed'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_quote', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Sub-title')),
                ('text', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Text')),
                ('author', models.CharField(max_length=254, verbose_name='Author')),
                ('author_title', models.CharField(max_length=254, verbose_name='Author - title')),
                ('author_image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Author - image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
