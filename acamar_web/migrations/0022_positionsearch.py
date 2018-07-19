# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0021_auto_20180717_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='PositionSearch',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_positionsearch', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('search_placeholder', models.CharField(max_length=254, verbose_name='Search input placeholder')),
                ('search_button', models.CharField(max_length=254, verbose_name='Search button text')),
                ('all_pacts_text', models.CharField(default='V\u0161echny \xfavazky', max_length=254, verbose_name='All jobs text')),
                ('recruiter_text', models.CharField(default='Provedu v\xe1s n\xe1borem', max_length=254, verbose_name='Recruiter text')),
                ('recruiter_email_text', models.CharField(default='Napi\u0161te mi e-mail', max_length=254, verbose_name='Recruiter email text')),
                ('more_button_text', models.CharField(max_length=254, verbose_name='More button text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
