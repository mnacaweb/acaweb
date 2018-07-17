# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0015_contactcard_contactgrid'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='author_cs',
            field=models.CharField(max_length=254, null=True, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='review',
            name='author_en',
            field=models.CharField(max_length=254, null=True, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='review',
            name='author_ru',
            field=models.CharField(max_length=254, null=True, verbose_name='Author'),
        ),
        migrations.AddField(
            model_name='review',
            name='text_cs',
            field=models.TextField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='review',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='review',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Text'),
        ),
    ]
