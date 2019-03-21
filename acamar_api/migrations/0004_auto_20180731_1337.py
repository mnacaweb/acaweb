# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("acamar_api", "0003_courseenroll_created")]

    operations = [
        migrations.RemoveField(model_name="course", name="main_banner_title"),
        migrations.RemoveField(model_name="course", name="main_banner_title_cs"),
        migrations.RemoveField(model_name="course", name="main_banner_title_en"),
        migrations.RemoveField(model_name="course", name="main_banner_title_ru"),
    ]
