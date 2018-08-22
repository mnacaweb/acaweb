# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('acamar_api', '0006_positionapply'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recruiter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('second_name', models.CharField(max_length=255, verbose_name='Second name')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'verbose_name': 'Recruiter',
                'verbose_name_plural': 'Recruiters',
            },
        ),
        migrations.AlterModelOptions(
            name='positionapply',
            options={'verbose_name': 'Position application', 'verbose_name_plural': 'Position application'},
        ),
        migrations.AlterUniqueTogether(
            name='recruiter',
            unique_together=set([('first_name', 'second_name')]),
        ),
    ]
