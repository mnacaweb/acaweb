# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def delete_coursepanelitems(apps, schema_editor):
    CourseTerm = apps.get_model("acamar_api", "CourseTerm")
    CourseTerm.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_api', '0007_auto_20180725_1507'),
    ]

    operations = [
        migrations.RunPython(delete_coursepanelitems),
        migrations.AddField(
            model_name='coursetermitem',
            name='parent',
            field=models.ForeignKey(related_name='items', verbose_name=b'Course term', to='acamar_api.CourseTerm'),
        ),
    ]
