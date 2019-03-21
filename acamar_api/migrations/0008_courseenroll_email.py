# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("acamar_api", "0007_auto_20180822_1010")]

    operations = [
        migrations.AddField(
            model_name="courseenroll",
            name="email",
            field=models.EmailField(default="", max_length=254, verbose_name="Email"),
            preserve_default=False,
        )
    ]
