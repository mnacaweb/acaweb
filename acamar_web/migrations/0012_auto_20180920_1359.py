# -*- coding: utf-8 -*-


from django.db import migrations, models
from django.db.models.expressions import F


def populate(apps, schema_editor):
    Link = apps.get_model("acamar_web", "Link")
    Link.objects.all().update(text_cs=F("text"))


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0011_courseenrollformmodel_email_label'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='text_cs',
            field=models.CharField(max_length=255, null=True, verbose_name='Link text'),
        ),
        migrations.AddField(
            model_name='link',
            name='text_en',
            field=models.CharField(max_length=255, null=True, verbose_name='Link text'),
        ),
        migrations.AddField(
            model_name='link',
            name='text_ru',
            field=models.CharField(max_length=255, null=True, verbose_name='Link text'),
        ),
        migrations.RunPython(populate)
    ]
