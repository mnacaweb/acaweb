# -*- coding: utf-8 -*-


from django.db import migrations, models
import django.db.models.deletion
import acamar_api.utils


class Migration(migrations.Migration):

    dependencies = [("acamar_api", "0005_auto_20180801_0931")]

    operations = [
        migrations.CreateModel(
            name="PositionApply",
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
                (
                    "position_name",
                    models.CharField(max_length=254, verbose_name="Position - name"),
                ),
                (
                    "position_user_name",
                    models.CharField(max_length=254, verbose_name="Position - person"),
                ),
                (
                    "position_user_email",
                    models.EmailField(
                        max_length=254, verbose_name="Position - person email"
                    ),
                ),
                (
                    "first_name",
                    models.CharField(max_length=254, verbose_name="First name"),
                ),
                (
                    "last_name",
                    models.CharField(max_length=254, verbose_name="Last name"),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Email")),
                ("phone", models.CharField(max_length=20, verbose_name="Phone")),
                (
                    "cv",
                    models.FileField(
                        upload_to=acamar_api.utils.cv_upload_to,
                        null=True,
                        verbose_name="CV",
                        blank=True,
                    ),
                ),
                (
                    "linkedin",
                    models.URLField(
                        max_length=254, verbose_name="LinkedIn", blank=True
                    ),
                ),
                ("text", models.TextField(verbose_name="Text", blank=True)),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="Created"),
                ),
                (
                    "position",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.SET_NULL,
                        verbose_name="Position",
                        blank=True,
                        to="acamar_api.Position",
                        null=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Position apply",
                "verbose_name_plural": "Position apply",
            },
        )
    ]
