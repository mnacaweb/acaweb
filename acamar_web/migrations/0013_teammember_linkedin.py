# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("acamar_web", "0012_auto_20180920_1359")]

    operations = [
        migrations.AddField(
            model_name="teammember",
            name="linkedin",
            field=models.URLField(verbose_name="LinkedIn link", blank=True),
        )
    ]
