# -*- coding: utf-8 -*-
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0015_auto_20190320_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainbanner',
            name='template',
            field=models.CharField(default='default', max_length=100, verbose_name='Template', choices=[('default', 'Default'), ('for_candidates', 'For candidates'), ('for_companies', 'For companies'), ('we_are', 'We are'), ('course', 'Course'), ('contact', 'Contact'), ('detail', 'Detail'), ('a-card', 'A-card'), ('enroll_in_course', 'Enroll in course'), ('private_policy', 'Privacy policy')]),
        ),
    ]
