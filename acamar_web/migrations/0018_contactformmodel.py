# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0017_auto_20180717_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_contactformmodel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=254, verbose_name='Sub-title')),
                ('name_label', models.CharField(max_length=254, verbose_name='Label - name')),
                ('email_label', models.CharField(max_length=254, verbose_name='Label - email')),
                ('purpose_label', models.CharField(max_length=254, verbose_name='Label - purpose')),
                ('text_label', models.CharField(max_length=254, verbose_name='Label - text')),
                ('button_text', models.CharField(max_length=254, verbose_name='Button text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
