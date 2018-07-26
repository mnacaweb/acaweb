# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0025_auto_20180726_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseGenericRegistration',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_coursegenericregistration', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('text', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Text')),
                ('button', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Button', to='acamar_web.Link')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterModelOptions(
            name='coursetermlistadditional',
            options={'verbose_name': 'Additional registration - item', 'verbose_name_plural': 'Additional registration - items'},
        ),
    ]
