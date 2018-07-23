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
        ('acamar_web', '0011_auto_20180723_1007'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_contactperson', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=254, verbose_name='Sub-title', blank=True)),
                ('person_name', models.CharField(max_length=254, verbose_name='Person name')),
                ('person_title', models.CharField(max_length=254, verbose_name='Person title')),
                ('person_phone', models.CharField(max_length=254, verbose_name='Person phone', blank=True)),
                ('button_text', models.CharField(max_length=254, verbose_name='Button text')),
                ('button_link_external', models.URLField(help_text='Provide a valid URL to an external website.', max_length=2040, verbose_name='Button external link', blank=True)),
                ('more_text', models.CharField(max_length=254, verbose_name='More link text', blank=True)),
                ('more_link_external', models.URLField(help_text='Provide a valid URL to an external website.', max_length=2040, verbose_name='More external link', blank=True)),
                ('button_link_internal', cms.models.fields.PageField(related_name='contact_people_button', blank=True, to='cms.Page', help_text='If provided, overrides the external link.', null=True, verbose_name='Button internal link')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
                ('more_link_internal', cms.models.fields.PageField(related_name='contact_people_more', blank=True, to='cms.Page', help_text='If provided, overrides the external link.', null=True, verbose_name='More internal link')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
