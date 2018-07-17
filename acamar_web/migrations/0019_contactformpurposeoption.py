# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0018_contactformmodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactFormPurposeOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254, verbose_name='Option name')),
                ('form', models.ForeignKey(related_name='purpose_options', editable=False, to='acamar_web.ContactFormModel')),
            ],
            options={
                'verbose_name': 'Option',
                'verbose_name_plural': 'Options',
            },
        ),
    ]
