# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_api', '0008_coursetermitem_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='main_banner',
            field=cms.models.fields.PlaceholderField(related_name='course_main_banner', slotname=b'main_banner', editable=False, to='cms.Placeholder', null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='content',
            field=cms.models.fields.PlaceholderField(related_name='course_content', slotname=b'course_content', editable=False, to='cms.Placeholder', null=True),
        ),
    ]
