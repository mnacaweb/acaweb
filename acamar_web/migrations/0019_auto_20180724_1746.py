# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0018_auto_20180724_1440'),
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Link name')),
                ('text', models.CharField(max_length=255, verbose_name='Link text')),
                ('external_link', models.URLField(help_text='Provide a valid URL to an external website.', max_length=2040, verbose_name='External link', blank=True)),
                ('mailto', models.EmailField(max_length=255, verbose_name='Email address', blank=True)),
                ('phone', models.CharField(max_length=255, verbose_name='Phone', blank=True)),
                ('target', models.CharField(blank=True, max_length=255, verbose_name='Target', choices=[('_blank', 'Open in new window'), ('_self', 'Open in same window'), ('_parent', 'Delegate to parent'), ('_top', 'Delegate to top')])),
                ('internal_link', cms.models.fields.PageField(blank=True, to='cms.Page', help_text='If provided, overrides the external link.', null=True, verbose_name='Internal link')),
            ],
        ),
        migrations.RemoveField(
            model_name='mainbannercard',
            name='button_link',
        ),
        migrations.RemoveField(
            model_name='mainbannercard',
            name='button_text',
        ),
        migrations.AddField(
            model_name='mainbannercard',
            name='button',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Button', blank=True, to='acamar_web.Link', null=True),
        ),
    ]
