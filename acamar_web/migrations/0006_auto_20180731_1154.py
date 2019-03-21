# -*- coding: utf-8 -*-


from django.db import migrations, models
import django.utils.translation


class Migration(migrations.Migration):

    dependencies = [("acamar_web", "0005_loginpluginmodel")]

    operations = [
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.AutoField(
                        verbose_name="ID",
                        serialize=False,
                        auto_created=True,
                        primary_key=True,
                    ),
                ),
                ("name", models.CharField(max_length=254, verbose_name="Name")),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("purpose", models.CharField(max_length=254, verbose_name="Purpose")),
                ("text", models.TextField(verbose_name="Text", blank=True)),
                (
                    "language",
                    models.CharField(
                        default=django.utils.translation.get_language,
                        max_length=3,
                        verbose_name="Language",
                        choices=[
                            ("cs", "\u010ce\u0161tina"),
                            ("en", "English"),
                            ("ru", "\u0440\u0443\u0441\u0441\u043a\u0438\u0439"),
                        ],
                    ),
                ),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
            ],
            options={"verbose_name": "Contact", "verbose_name_plural": "Contacts"},
        ),
        migrations.AddField(
            model_name="contactformmodel",
            name="success_text",
            field=models.CharField(
                default="Ozveme se v\xe1m co nejd\u0159\xedve",
                max_length=254,
                verbose_name="Success text",
            ),
            preserve_default=False,
        ),
    ]
