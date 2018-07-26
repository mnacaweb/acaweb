# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_api', '0011_auto_20180726_1239'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='main_banner_title',
            field=models.CharField(default='Z\xedskejte z\xe1kladn\xed znalosti pro pozici testera', max_length=254, verbose_name='Main banner title'),
            preserve_default=False,
        ),
    ]
