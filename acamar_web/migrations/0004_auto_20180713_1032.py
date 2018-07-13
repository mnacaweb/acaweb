# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0003_workelipse_workelipsecolumn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainbanner',
            name='title',
            field=models.CharField(max_length=254, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='mainbannercard',
            name='title',
            field=models.CharField(max_length=254, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='workelipse',
            name='title',
            field=models.CharField(max_length=254, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='workelipsecolumn',
            name='title',
            field=models.CharField(max_length=254, verbose_name='Title'),
        ),
    ]
