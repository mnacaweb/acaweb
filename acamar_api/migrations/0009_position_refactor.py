# -*- coding: utf-8 -*-


from django.db import migrations, models


def delete_model(apps, schema_editor):
    Position = apps.get_model("acamar_api", "Position")
    Position.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [("acamar_api", "0008_courseenroll_email")]

    operations = [
        migrations.RunPython(delete_model, reverse_code=lambda x, y: None),
        migrations.AddField(
            model_name="position",
            name="internal_id",
            field=models.PositiveIntegerField(db_index=True),
        ),
        migrations.AlterField(
            model_name="position",
            name="lang",
            field=models.CharField(
                db_index=True,
                max_length=3,
                choices=[
                    ("cs", "\u010ce\u0161tina"),
                    ("en", "English"),
                    ("ru", "\u0440\u0443\u0441\u0441\u043a\u0438\u0439"),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="pacts",
            field=models.ManyToManyField(
                related_name="positions", to="acamar_api.PositionPact", blank=True
            ),
        ),
        migrations.AlterField(
            model_name="position",
            name="slug",
            field=models.SlugField(max_length=120, blank=True),
        ),
        migrations.AlterField(
            model_name="position",
            name="technologies",
            field=models.ManyToManyField(
                related_name="positions", to="acamar_api.PositionTechnology", blank=True
            ),
        ),
        migrations.AlterUniqueTogether(
            name="position", unique_together=set([("lang", "internal_id")])
        ),
        migrations.RemoveField(model_name="position", name="introduction_cs"),
        migrations.RemoveField(model_name="position", name="introduction_en"),
        migrations.RemoveField(model_name="position", name="introduction_ru"),
        migrations.RemoveField(model_name="position", name="lang_cs"),
        migrations.RemoveField(model_name="position", name="lang_en"),
        migrations.RemoveField(model_name="position", name="lang_ru"),
        migrations.RemoveField(model_name="position", name="name_cs"),
        migrations.RemoveField(model_name="position", name="name_en"),
        migrations.RemoveField(model_name="position", name="name_ru"),
        migrations.RemoveField(model_name="position", name="place_cs"),
        migrations.RemoveField(model_name="position", name="place_en"),
        migrations.RemoveField(model_name="position", name="place_ru"),
        migrations.RemoveField(model_name="position", name="slug_cs"),
        migrations.RemoveField(model_name="position", name="slug_en"),
        migrations.RemoveField(model_name="position", name="slug_ru"),
        migrations.RemoveField(model_name="position", name="start_cs"),
        migrations.RemoveField(model_name="position", name="start_en"),
        migrations.RemoveField(model_name="position", name="start_ru"),
        migrations.RemoveField(model_name="position", name="text1_cs"),
        migrations.RemoveField(model_name="position", name="text1_en"),
        migrations.RemoveField(model_name="position", name="text1_ru"),
        migrations.RemoveField(model_name="position", name="text2_cs"),
        migrations.RemoveField(model_name="position", name="text2_en"),
        migrations.RemoveField(model_name="position", name="text2_ru"),
        migrations.RemoveField(model_name="position", name="text3_cs"),
        migrations.RemoveField(model_name="position", name="text3_en"),
        migrations.RemoveField(model_name="position", name="text3_ru"),
        migrations.RemoveField(model_name="position", name="text4_cs"),
        migrations.RemoveField(model_name="position", name="text4_en"),
        migrations.RemoveField(model_name="position", name="text4_ru"),
        migrations.RemoveField(model_name="position", name="text5_cs"),
        migrations.RemoveField(model_name="position", name="text5_en"),
        migrations.RemoveField(model_name="position", name="text5_ru"),
        migrations.RemoveField(model_name="position", name="text6_cs"),
        migrations.RemoveField(model_name="position", name="text6_en"),
        migrations.RemoveField(model_name="position", name="text6_ru"),
        migrations.RemoveField(model_name="position", name="title1_cs"),
        migrations.RemoveField(model_name="position", name="title1_en"),
        migrations.RemoveField(model_name="position", name="title1_ru"),
        migrations.RemoveField(model_name="position", name="title2_cs"),
        migrations.RemoveField(model_name="position", name="title2_en"),
        migrations.RemoveField(model_name="position", name="title2_ru"),
        migrations.RemoveField(model_name="position", name="title3_cs"),
        migrations.RemoveField(model_name="position", name="title3_en"),
        migrations.RemoveField(model_name="position", name="title3_ru"),
        migrations.RemoveField(model_name="position", name="title4_cs"),
        migrations.RemoveField(model_name="position", name="title4_en"),
        migrations.RemoveField(model_name="position", name="title4_ru"),
        migrations.RemoveField(model_name="position", name="title5_cs"),
        migrations.RemoveField(model_name="position", name="title5_en"),
        migrations.RemoveField(model_name="position", name="title5_ru"),
        migrations.RemoveField(model_name="position", name="title6_cs"),
        migrations.RemoveField(model_name="position", name="title6_en"),
        migrations.RemoveField(model_name="position", name="title6_ru"),
        migrations.RemoveField(model_name="position", name="user_position_cs"),
        migrations.RemoveField(model_name="position", name="user_position_en"),
        migrations.RemoveField(model_name="position", name="user_position_ru"),
        migrations.RenameField(
            model_name="position", old_name="user_image_url", new_name="_user_image_url"
        ),
        migrations.AlterField(
            model_name="position",
            name="_user_image_url",
            field=models.URLField(
                max_length=254, db_column="user_image_url", blank=True
            ),
        ),
        migrations.RunPython(lambda x, y: None, reverse_code=delete_model),
    ]
