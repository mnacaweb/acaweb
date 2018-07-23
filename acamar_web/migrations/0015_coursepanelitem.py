# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0014_coursepanel_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePanelItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('_course', models.PositiveIntegerField(verbose_name='Course')),
                ('course_panel', models.ForeignKey(related_name='items', to='acamar_web.CoursePanel')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
    ]
