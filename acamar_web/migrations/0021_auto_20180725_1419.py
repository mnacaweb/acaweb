# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def delete_coursepanelitems(apps, schema_editor):
    CoursePanelItem = apps.get_model("acamar_web", "CoursePanelItem")
    CoursePanelItem.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_api', '0006_courseterm'),
        ('acamar_web', '0020_auto_20180725_1111'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='coursepanelitem',
            name='_course',
        ),
        migrations.RunPython(delete_coursepanelitems),
        migrations.AddField(
            model_name='coursepanelitem',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Course', to='acamar_api.Course'),
        ),
    ]
