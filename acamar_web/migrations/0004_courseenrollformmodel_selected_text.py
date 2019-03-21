# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("acamar_web", "0003_auto_20180727_1406")]

    operations = [
        migrations.AddField(
            model_name="courseenrollformmodel",
            name="selected_text",
            field=models.CharField(
                default="vybr\xe1no",
                max_length=30,
                verbose_name="Multi-select selected text",
            ),
        )
    ]
