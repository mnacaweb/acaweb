# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('acamar_web', '0013_auto_20180716_1650'),
    ]

    operations = [
        migrations.AddField(
            model_name='teammember',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, default=7, verbose_name='Image', to=settings.FILER_IMAGE_MODEL),
            preserve_default=False,
        ),
    ]
