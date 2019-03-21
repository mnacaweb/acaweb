# -*- coding: utf-8 -*-


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0002_partnersitem'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseEnrollFormModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_courseenrollformmodel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.CASCADE)),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('name_label', models.CharField(max_length=254, verbose_name='Name label')),
                ('phone_label', models.CharField(max_length=254, verbose_name='Phone label')),
                ('course_label', models.CharField(max_length=254, verbose_name='Course select label')),
                ('expectations_label', models.CharField(max_length=254, verbose_name='Expectations label')),
                ('cv_label', models.CharField(max_length=254, verbose_name='CV label')),
                ('submit_text', models.CharField(max_length=254, verbose_name='Submit button text')),
                ('email_button', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Email link', blank=True, to='acamar_web.Link', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='mainbanner',
            name='template',
            field=models.CharField(default='default', max_length=100, verbose_name='Template', choices=[('default', 'Default'), ('for_candidates', 'For candidates'), ('for_companies', 'For companies'), ('we_are', 'We are'), ('course', 'Course'), ('contact', 'Contact'), ('detail', 'Detail'), ('a-card', 'A-card'), ('enroll_in_course', 'Enroll in course')]),
        ),
    ]
