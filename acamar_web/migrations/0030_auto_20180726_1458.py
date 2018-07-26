# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


def delete_coursetermlist(apps, schema_editor):
    CourseTermList = apps.get_model("acamar_web", "CourseTermList")
    CourseTermList.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0029_coursetermlist_additional_button'),
    ]

    operations = [
        migrations.RunPython(delete_coursetermlist),
        migrations.RemoveField(
            model_name='coursetermlist',
            name='additional_button',
        ),
        migrations.RemoveField(
            model_name='coursetermlist',
            name='register_button_text',
        ),
        migrations.AddField(
            model_name='coursetermlist',
            name='button',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Registration button', to='acamar_web.Link'),
        ),
    ]
