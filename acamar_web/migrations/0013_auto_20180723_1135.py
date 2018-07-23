# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0012_contactperson'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursepanel',
            name='button_link',
        ),
        migrations.AddField(
            model_name='coursepanel',
            name='button_link_external',
            field=models.URLField(help_text='Provide a valid URL to an external website.', max_length=2040, verbose_name='External link', blank=True),
        ),
        migrations.AddField(
            model_name='coursepanel',
            name='button_link_internal',
            field=cms.models.fields.PageField(blank=True, to='cms.Page', help_text='If provided, overrides the external link.', null=True, verbose_name='Internal link'),
        ),
        migrations.AlterField(
            model_name='coursepanel',
            name='button_text',
            field=models.CharField(max_length=254, verbose_name='Button text', blank=True),
        ),
        migrations.AlterField(
            model_name='mainbanner',
            name='subtitle',
            field=models.TextField(verbose_name='Sub-title', blank=True),
        ),
    ]
