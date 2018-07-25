# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0019_auto_20180724_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactperson',
            name='button_link_external',
        ),
        migrations.RemoveField(
            model_name='contactperson',
            name='button_link_internal',
        ),
        migrations.RemoveField(
            model_name='contactperson',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='contactperson',
            name='more_link_external',
        ),
        migrations.RemoveField(
            model_name='contactperson',
            name='more_link_internal',
        ),
        migrations.RemoveField(
            model_name='contactperson',
            name='more_text',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='link_external',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='link_internal',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='link_text',
        ),
        migrations.RemoveField(
            model_name='coursepanel',
            name='button_link_external',
        ),
        migrations.RemoveField(
            model_name='coursepanel',
            name='button_link_internal',
        ),
        migrations.RemoveField(
            model_name='coursepanel',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='graphsection',
            name='button_link_external',
        ),
        migrations.RemoveField(
            model_name='graphsection',
            name='button_link_internal',
        ),
        migrations.RemoveField(
            model_name='graphsection',
            name='button_text',
        ),
        migrations.RemoveField(
            model_name='logopanel',
            name='button_link',
        ),
        migrations.RemoveField(
            model_name='logopanel',
            name='button_text',
        ),
        migrations.AddField(
            model_name='contactperson',
            name='button',
            field=models.ForeignKey(related_name='contact_person_button_set', on_delete=django.db.models.deletion.PROTECT, verbose_name='Button', blank=True, to='acamar_web.Link', null=True),
        ),
        migrations.AddField(
            model_name='contactperson',
            name='more',
            field=models.ForeignKey(related_name='contact_person_more_set', on_delete=django.db.models.deletion.PROTECT, verbose_name='More link', blank=True, to='acamar_web.Link', null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='additional_link',
            field=models.ForeignKey(related_name='contact_us_additional_set', on_delete=django.db.models.deletion.PROTECT, verbose_name='Additional link', blank=True, to='acamar_web.Link', null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='button',
            field=models.ForeignKey(related_name='contact_us_button_set', on_delete=django.db.models.deletion.PROTECT, verbose_name='Button', blank=True, to='acamar_web.Link', null=True),
        ),
        migrations.AddField(
            model_name='coursepanel',
            name='button',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Button', blank=True, to='acamar_web.Link', null=True),
        ),
        migrations.AddField(
            model_name='graphsection',
            name='button',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Button', blank=True, to='acamar_web.Link', null=True),
        ),
        migrations.AddField(
            model_name='logopanel',
            name='button',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Button', blank=True, to='acamar_web.Link', null=True),
        ),
    ]
