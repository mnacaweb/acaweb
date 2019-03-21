# -*- coding: utf-8 -*-


from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [("acamar_api", "0002_auto_20180730_1115")]

    operations = [
        migrations.AddField(
            model_name="courseenroll",
            name="created",
            field=models.DateTimeField(
                default=datetime.datetime(2018, 7, 31, 11, 20, 42, 253012, tzinfo=utc),
                verbose_name="Created",
                auto_now_add=True,
            ),
            preserve_default=False,
        )
    ]
