# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0024_auto_20180726_1010'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseTermListAdditional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=254, verbose_name='Address', blank=True)),
                ('description', models.CharField(max_length=254, verbose_name='Description', blank=True)),
            ],
            options={
                'verbose_name': 'Course term list additional item',
                'verbose_name_plural': 'Course term list additional items',
            },
        ),
        migrations.AddField(
            model_name='coursetermlist',
            name='register_button_text',
            field=models.CharField(default='P\u0159ihl\xe1sit se', max_length=254, verbose_name='Register button text'),
        ),
        migrations.AlterField(
            model_name='coursetermlist',
            name='additional_registration',
            field=models.BooleanField(default=False, verbose_name='Additional registration'),
        ),
        migrations.AddField(
            model_name='coursetermlistadditional',
            name='parent',
            field=models.ForeignKey(related_name='additional_items', to='acamar_web.CourseTermList'),
        ),
    ]
