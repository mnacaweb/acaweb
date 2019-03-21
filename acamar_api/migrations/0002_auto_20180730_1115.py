# -*- coding: utf-8 -*-


from django.db import migrations, models
import acamar_api.utils


class Migration(migrations.Migration):

    dependencies = [("acamar_api", "0001_squashed2")]

    operations = [
        migrations.CreateModel(
            name="CourseEnroll",
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
                ("phone", models.CharField(max_length=20, verbose_name="Phone")),
                (
                    "expectations",
                    models.TextField(verbose_name="Expectations", blank=True),
                ),
                (
                    "cv",
                    models.FileField(
                        upload_to=acamar_api.utils.cv_upload_to,
                        null=True,
                        verbose_name="CV",
                        blank=True,
                    ),
                ),
            ],
            options={
                "verbose_name": "Course registration",
                "verbose_name_plural": "Course registrations",
            },
        ),
        migrations.AddField(
            model_name="course",
            name="deleted",
            field=models.DateTimeField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name="courseterm",
            name="deleted",
            field=models.DateTimeField(null=True, editable=False),
        ),
        migrations.AddField(
            model_name="courseenroll",
            name="courses",
            field=models.ManyToManyField(
                related_name="enrolled",
                verbose_name="Course terms",
                to="acamar_api.CourseTerm",
            ),
        ),
    ]
