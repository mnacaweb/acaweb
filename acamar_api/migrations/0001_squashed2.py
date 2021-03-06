# -*- coding: utf-8 -*-


from django.db import migrations, models
import djangocms_text_ckeditor.fields
import meta.models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [("cms", "0020_old_tree_cleanup")]

    operations = [
        migrations.CreateModel(
            name="Course",
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
                ("title", models.CharField(max_length=254, verbose_name="Title")),
                (
                    "title_cs",
                    models.CharField(max_length=254, null=True, verbose_name="Title"),
                ),
                (
                    "title_en",
                    models.CharField(max_length=254, null=True, verbose_name="Title"),
                ),
                (
                    "title_ru",
                    models.CharField(max_length=254, null=True, verbose_name="Title"),
                ),
                ("slug", models.SlugField(verbose_name="Url-slug")),
                ("slug_cs", models.SlugField(null=True, verbose_name="Url-slug")),
                ("slug_en", models.SlugField(null=True, verbose_name="Url-slug")),
                ("slug_ru", models.SlugField(null=True, verbose_name="Url-slug")),
                (
                    "main_banner_title",
                    models.CharField(max_length=254, verbose_name="Main banner title"),
                ),
                (
                    "main_banner_title_cs",
                    models.CharField(
                        max_length=254, null=True, verbose_name="Main banner title"
                    ),
                ),
                (
                    "main_banner_title_en",
                    models.CharField(
                        max_length=254, null=True, verbose_name="Main banner title"
                    ),
                ),
                (
                    "main_banner_title_ru",
                    models.CharField(
                        max_length=254, null=True, verbose_name="Main banner title"
                    ),
                ),
                (
                    "short_description",
                    models.TextField(verbose_name="Short description"),
                ),
                (
                    "short_description_cs",
                    models.TextField(null=True, verbose_name="Short description"),
                ),
                (
                    "short_description_en",
                    models.TextField(null=True, verbose_name="Short description"),
                ),
                (
                    "short_description_ru",
                    models.TextField(null=True, verbose_name="Short description"),
                ),
                (
                    "place",
                    models.CharField(max_length=254, verbose_name="Place", blank=True),
                ),
                (
                    "place_cs",
                    models.CharField(
                        max_length=254, null=True, verbose_name="Place", blank=True
                    ),
                ),
                (
                    "place_en",
                    models.CharField(
                        max_length=254, null=True, verbose_name="Place", blank=True
                    ),
                ),
                (
                    "place_ru",
                    models.CharField(
                        max_length=254, null=True, verbose_name="Place", blank=True
                    ),
                ),
                (
                    "price",
                    models.PositiveIntegerField(
                        null=True, verbose_name="Price", blank=True
                    ),
                ),
                (
                    "price_cs",
                    models.PositiveIntegerField(
                        null=True, verbose_name="Price", blank=True
                    ),
                ),
                (
                    "price_en",
                    models.PositiveIntegerField(
                        null=True, verbose_name="Price", blank=True
                    ),
                ),
                (
                    "price_ru",
                    models.PositiveIntegerField(
                        null=True, verbose_name="Price", blank=True
                    ),
                ),
                (
                    "duration",
                    models.CharField(
                        max_length=254, verbose_name="Duration", blank=True
                    ),
                ),
                (
                    "duration_cs",
                    models.CharField(
                        max_length=254, null=True, verbose_name="Duration", blank=True
                    ),
                ),
                (
                    "duration_en",
                    models.CharField(
                        max_length=254, null=True, verbose_name="Duration", blank=True
                    ),
                ),
                (
                    "duration_ru",
                    models.CharField(
                        max_length=254, null=True, verbose_name="Duration", blank=True
                    ),
                ),
                (
                    "meta_keywords",
                    models.CharField(
                        max_length=254, verbose_name="Meta keywords", blank=True
                    ),
                ),
                (
                    "meta_keywords_cs",
                    models.CharField(
                        max_length=254,
                        null=True,
                        verbose_name="Meta keywords",
                        blank=True,
                    ),
                ),
                (
                    "meta_keywords_en",
                    models.CharField(
                        max_length=254,
                        null=True,
                        verbose_name="Meta keywords",
                        blank=True,
                    ),
                ),
                (
                    "meta_keywords_ru",
                    models.CharField(
                        max_length=254,
                        null=True,
                        verbose_name="Meta keywords",
                        blank=True,
                    ),
                ),
                (
                    "content",
                    cms.models.fields.PlaceholderField(
                        related_name="course_content",
                        slotname="course_content",
                        editable=False,
                        to="cms.Placeholder",
                        null=True,
                    ),
                ),
                (
                    "main_banner",
                    cms.models.fields.PlaceholderField(
                        related_name="course_main_banner",
                        slotname="main_banner",
                        editable=False,
                        to="cms.Placeholder",
                        null=True,
                    ),
                ),
            ],
            options={"verbose_name": "Course", "verbose_name_plural": "Courses"},
            bases=(meta.models.ModelMeta, models.Model),
        ),
        migrations.CreateModel(
            name="CourseTerm",
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
                    "course",
                    models.ForeignKey(
                        related_name="terms",
                        verbose_name="Course",
                        to="acamar_api.Course",
                        on_delete=models.CASCADE,
                    ),
                ),
            ],
            options={
                "verbose_name": "Course term",
                "verbose_name_plural": "Course terms",
            },
        ),
        migrations.CreateModel(
            name="CourseTermItem",
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
                ("date", models.DateField(verbose_name="Date")),
                ("start_time", models.TimeField(verbose_name="Start time")),
                (
                    "end_time",
                    models.TimeField(null=True, verbose_name="End time", blank=True),
                ),
                (
                    "address",
                    models.CharField(
                        max_length=254, verbose_name="Address", blank=True
                    ),
                ),
                (
                    "address_cs",
                    models.CharField(
                        max_length=254, null=True, verbose_name="Address", blank=True
                    ),
                ),
                (
                    "address_en",
                    models.CharField(
                        max_length=254, null=True, verbose_name="Address", blank=True
                    ),
                ),
                (
                    "address_ru",
                    models.CharField(
                        max_length=254, null=True, verbose_name="Address", blank=True
                    ),
                ),
                (
                    "description",
                    models.CharField(
                        max_length=254, verbose_name="Description", blank=True
                    ),
                ),
                (
                    "description_cs",
                    models.CharField(
                        max_length=254,
                        null=True,
                        verbose_name="Description",
                        blank=True,
                    ),
                ),
                (
                    "description_en",
                    models.CharField(
                        max_length=254,
                        null=True,
                        verbose_name="Description",
                        blank=True,
                    ),
                ),
                (
                    "description_ru",
                    models.CharField(
                        max_length=254,
                        null=True,
                        verbose_name="Description",
                        blank=True,
                    ),
                ),
                (
                    "parent",
                    models.ForeignKey(
                        related_name="items",
                        verbose_name="Course term",
                        to="acamar_api.CourseTerm",
                        on_delete=models.CASCADE,
                    ),
                ),
            ],
            options={
                "verbose_name": "Course term - item",
                "verbose_name_plural": "Course term - items",
            },
        ),
        migrations.CreateModel(
            name="Position",
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
                ("lang", models.BooleanField(default=False, db_index=True)),
                ("lang_cs", models.BooleanField(default=False, db_index=True)),
                ("lang_en", models.BooleanField(default=False, db_index=True)),
                ("lang_ru", models.BooleanField(default=False, db_index=True)),
                ("date", models.DateTimeField()),
                ("place", models.CharField(max_length=254, blank=True)),
                ("place_cs", models.CharField(max_length=254, null=True, blank=True)),
                ("place_en", models.CharField(max_length=254, null=True, blank=True)),
                ("place_ru", models.CharField(max_length=254, null=True, blank=True)),
                ("start", models.CharField(max_length=254, blank=True)),
                ("start_cs", models.CharField(max_length=254, null=True, blank=True)),
                ("start_en", models.CharField(max_length=254, null=True, blank=True)),
                ("start_ru", models.CharField(max_length=254, null=True, blank=True)),
                ("name", models.CharField(max_length=254, blank=True)),
                ("name_cs", models.CharField(max_length=254, null=True, blank=True)),
                ("name_en", models.CharField(max_length=254, null=True, blank=True)),
                ("name_ru", models.CharField(max_length=254, null=True, blank=True)),
                ("slug", models.SlugField(max_length=120, blank=True)),
                ("slug_cs", models.SlugField(max_length=120, null=True, blank=True)),
                ("slug_en", models.SlugField(max_length=120, null=True, blank=True)),
                ("slug_ru", models.SlugField(max_length=120, null=True, blank=True)),
                ("introduction", models.TextField(blank=True)),
                ("introduction_cs", models.TextField(null=True, blank=True)),
                ("introduction_en", models.TextField(null=True, blank=True)),
                ("introduction_ru", models.TextField(null=True, blank=True)),
                ("title1", models.CharField(max_length=254, blank=True)),
                ("title1_cs", models.CharField(max_length=254, null=True, blank=True)),
                ("title1_en", models.CharField(max_length=254, null=True, blank=True)),
                ("title1_ru", models.CharField(max_length=254, null=True, blank=True)),
                ("text1", djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                (
                    "text1_cs",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                (
                    "text1_en",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                (
                    "text1_ru",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                ("title2", models.CharField(max_length=254, blank=True)),
                ("title2_cs", models.CharField(max_length=254, null=True, blank=True)),
                ("title2_en", models.CharField(max_length=254, null=True, blank=True)),
                ("title2_ru", models.CharField(max_length=254, null=True, blank=True)),
                ("text2", djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                (
                    "text2_cs",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                (
                    "text2_en",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                (
                    "text2_ru",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                ("title3", models.CharField(max_length=254, blank=True)),
                ("title3_cs", models.CharField(max_length=254, null=True, blank=True)),
                ("title3_en", models.CharField(max_length=254, null=True, blank=True)),
                ("title3_ru", models.CharField(max_length=254, null=True, blank=True)),
                ("text3", djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                (
                    "text3_cs",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                (
                    "text3_en",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                (
                    "text3_ru",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                ("title4", models.CharField(max_length=254, blank=True)),
                ("title4_cs", models.CharField(max_length=254, null=True, blank=True)),
                ("title4_en", models.CharField(max_length=254, null=True, blank=True)),
                ("title4_ru", models.CharField(max_length=254, null=True, blank=True)),
                ("text4", djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                (
                    "text4_cs",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                (
                    "text4_en",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                (
                    "text4_ru",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                ("title5", models.CharField(max_length=254, blank=True)),
                ("title5_cs", models.CharField(max_length=254, null=True, blank=True)),
                ("title5_en", models.CharField(max_length=254, null=True, blank=True)),
                ("title5_ru", models.CharField(max_length=254, null=True, blank=True)),
                ("text5", djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                (
                    "text5_cs",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                (
                    "text5_en",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                (
                    "text5_ru",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                ("title6", models.CharField(max_length=254, blank=True)),
                ("title6_cs", models.CharField(max_length=254, null=True, blank=True)),
                ("title6_en", models.CharField(max_length=254, null=True, blank=True)),
                ("title6_ru", models.CharField(max_length=254, null=True, blank=True)),
                ("text6", djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                (
                    "text6_cs",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                (
                    "text6_en",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                (
                    "text6_ru",
                    djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True),
                ),
                ("user_email", models.CharField(max_length=254, blank=True)),
                ("user_first_name", models.CharField(max_length=254, blank=True)),
                ("user_second_name", models.CharField(max_length=254, blank=True)),
                ("user_image", models.CharField(max_length=254, blank=True)),
                ("user_image_url", models.URLField(max_length=254, blank=True)),
                ("user_phone", models.CharField(max_length=254, blank=True)),
                ("user_position", models.CharField(max_length=254, blank=True)),
                (
                    "user_position_cs",
                    models.CharField(max_length=254, null=True, blank=True),
                ),
                (
                    "user_position_en",
                    models.CharField(max_length=254, null=True, blank=True),
                ),
                (
                    "user_position_ru",
                    models.CharField(max_length=254, null=True, blank=True),
                ),
            ],
            options={"verbose_name": "Position", "verbose_name_plural": "Positions"},
            bases=(meta.models.ModelMeta, models.Model),
        ),
        migrations.CreateModel(
            name="PositionCategory",
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
                (
                    "name_cs",
                    models.CharField(max_length=254, null=True, verbose_name="Name"),
                ),
                (
                    "name_en",
                    models.CharField(max_length=254, null=True, verbose_name="Name"),
                ),
                (
                    "name_ru",
                    models.CharField(max_length=254, null=True, verbose_name="Name"),
                ),
            ],
            options={
                "verbose_name": "Position category",
                "verbose_name_plural": "Position categories",
            },
        ),
        migrations.CreateModel(
            name="PositionPact",
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
                (
                    "name_cs",
                    models.CharField(max_length=254, null=True, verbose_name="Name"),
                ),
                (
                    "name_en",
                    models.CharField(max_length=254, null=True, verbose_name="Name"),
                ),
                (
                    "name_ru",
                    models.CharField(max_length=254, null=True, verbose_name="Name"),
                ),
            ],
            options={
                "verbose_name": "Position pact",
                "verbose_name_plural": "Position pacts",
            },
        ),
        migrations.CreateModel(
            name="PositionTechnology",
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
                (
                    "name_cs",
                    models.CharField(max_length=254, null=True, verbose_name="Name"),
                ),
                (
                    "name_en",
                    models.CharField(max_length=254, null=True, verbose_name="Name"),
                ),
                (
                    "name_ru",
                    models.CharField(max_length=254, null=True, verbose_name="Name"),
                ),
            ],
            options={
                "verbose_name": "Position technology",
                "verbose_name_plural": "Position technologies",
            },
        ),
        migrations.AddField(
            model_name="position",
            name="category",
            field=models.ForeignKey(
                related_name="positions",
                to="acamar_api.PositionCategory",
                on_delete=models.CASCADE,
            ),
        ),
        migrations.AddField(
            model_name="position",
            name="pacts",
            field=models.ManyToManyField(
                related_name="positions", to="acamar_api.PositionPact"
            ),
        ),
        migrations.AddField(
            model_name="position",
            name="technologies",
            field=models.ManyToManyField(
                related_name="positions", to="acamar_api.PositionTechnology"
            ),
        ),
    ]
