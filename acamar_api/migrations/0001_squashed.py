# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    replaces = [('acamar_api', '0001_initial'), ('acamar_api', '0002_auto_20180717_1656'), ('acamar_api', '0003_auto_20180717_1746'), ('acamar_api', '0004_auto_20180717_1753')]

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PositionCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254, verbose_name=b'Name')),
                ('name_cs', models.CharField(max_length=254, null=True, verbose_name=b'Name')),
                ('name_en', models.CharField(max_length=254, null=True, verbose_name=b'Name')),
                ('name_ru', models.CharField(max_length=254, null=True, verbose_name=b'Name')),
            ],
            options={
                'verbose_name': 'Position category',
                'verbose_name_plural': 'Position categories',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField()),
                ('place', models.CharField(max_length=254, blank=True)),
                ('place_cs', models.CharField(max_length=254, null=True, blank=True)),
                ('place_en', models.CharField(max_length=254, null=True, blank=True)),
                ('place_ru', models.CharField(max_length=254, null=True, blank=True)),
                ('start', models.CharField(max_length=254, blank=True)),
                ('start_cs', models.CharField(max_length=254, null=True, blank=True)),
                ('start_en', models.CharField(max_length=254, null=True, blank=True)),
                ('start_ru', models.CharField(max_length=254, null=True, blank=True)),
                ('name', models.CharField(max_length=254, blank=True)),
                ('name_cs', models.CharField(max_length=254, null=True, blank=True)),
                ('name_en', models.CharField(max_length=254, null=True, blank=True)),
                ('name_ru', models.CharField(max_length=254, null=True, blank=True)),
                ('introduction', models.TextField(blank=True)),
                ('introduction_cs', models.TextField(null=True, blank=True)),
                ('introduction_en', models.TextField(null=True, blank=True)),
                ('introduction_ru', models.TextField(null=True, blank=True)),
                ('title1', models.CharField(max_length=254, blank=True)),
                ('title1_cs', models.CharField(max_length=254, null=True, blank=True)),
                ('title1_en', models.CharField(max_length=254, null=True, blank=True)),
                ('title1_ru', models.CharField(max_length=254, null=True, blank=True)),
                ('text1', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('text1_cs', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('text1_en', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('text1_ru', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('title2', models.CharField(max_length=254, blank=True)),
                ('title2_cs', models.CharField(max_length=254, null=True, blank=True)),
                ('title2_en', models.CharField(max_length=254, null=True, blank=True)),
                ('title2_ru', models.CharField(max_length=254, null=True, blank=True)),
                ('text2', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('text2_cs', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('text2_en', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('text2_ru', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('title3', models.CharField(max_length=254, blank=True)),
                ('title3_cs', models.CharField(max_length=254, null=True, blank=True)),
                ('title3_en', models.CharField(max_length=254, null=True, blank=True)),
                ('title3_ru', models.CharField(max_length=254, null=True, blank=True)),
                ('text3', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('text3_cs', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('text3_en', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('text3_ru', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('title4', models.CharField(max_length=254, blank=True)),
                ('title4_cs', models.CharField(max_length=254, null=True, blank=True)),
                ('title4_en', models.CharField(max_length=254, null=True, blank=True)),
                ('title4_ru', models.CharField(max_length=254, null=True, blank=True)),
                ('text4', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('text4_cs', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('text4_en', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('text4_ru', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('title5', models.CharField(max_length=254, blank=True)),
                ('title5_cs', models.CharField(max_length=254, null=True, blank=True)),
                ('title5_en', models.CharField(max_length=254, null=True, blank=True)),
                ('title5_ru', models.CharField(max_length=254, null=True, blank=True)),
                ('text5', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('text5_cs', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('text5_en', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('text5_ru', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('title6', models.CharField(max_length=254, blank=True)),
                ('title6_cs', models.CharField(max_length=254, null=True, blank=True)),
                ('title6_en', models.CharField(max_length=254, null=True, blank=True)),
                ('title6_ru', models.CharField(max_length=254, null=True, blank=True)),
                ('text6', djangocms_text_ckeditor.fields.HTMLField(blank=True)),
                ('text6_cs', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('text6_en', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('text6_ru', djangocms_text_ckeditor.fields.HTMLField(null=True, blank=True)),
                ('user_email', models.CharField(max_length=254, blank=True)),
                ('user_first_name', models.CharField(max_length=254, blank=True)),
                ('user_second_name', models.CharField(max_length=254, blank=True)),
                ('user_image', models.CharField(max_length=254, blank=True)),
                ('user_image_url', models.URLField(max_length=254, blank=True)),
                ('user_phone', models.CharField(max_length=254, blank=True)),
                ('user_position', models.CharField(max_length=254, blank=True)),
                ('user_position_cs', models.CharField(max_length=254, null=True, blank=True)),
                ('user_position_en', models.CharField(max_length=254, null=True, blank=True)),
                ('user_position_ru', models.CharField(max_length=254, null=True, blank=True)),
                ('category', models.ForeignKey(related_name='positions', to='acamar_api.PositionCategory')),
            ],
            options={
                'verbose_name': 'Position',
                'verbose_name_plural': 'Positions',
            },
        ),
        migrations.CreateModel(
            name='PositionPact',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254, verbose_name=b'Name')),
                ('name_cs', models.CharField(max_length=254, null=True, verbose_name=b'Name')),
                ('name_en', models.CharField(max_length=254, null=True, verbose_name=b'Name')),
                ('name_ru', models.CharField(max_length=254, null=True, verbose_name=b'Name')),
            ],
            options={
                'verbose_name': 'Position pact',
                'verbose_name_plural': 'Position pacts',
            },
        ),
        migrations.CreateModel(
            name='PositionTechnology',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254, verbose_name=b'Name')),
                ('name_cs', models.CharField(max_length=254, null=True, verbose_name=b'Name')),
                ('name_en', models.CharField(max_length=254, null=True, verbose_name=b'Name')),
                ('name_ru', models.CharField(max_length=254, null=True, verbose_name=b'Name')),
            ],
            options={
                'verbose_name': 'Position technology',
                'verbose_name_plural': 'Position technologies',
            },
        ),
        migrations.AddField(
            model_name='position',
            name='pacts',
            field=models.ManyToManyField(related_name='positions', to=b'acamar_api.PositionPact'),
        ),
        migrations.AddField(
            model_name='position',
            name='technologies',
            field=models.ManyToManyField(related_name='positions', to=b'acamar_api.PositionTechnology'),
        ),
        migrations.AddField(
            model_name='position',
            name='lang',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AddField(
            model_name='position',
            name='lang_cs',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AddField(
            model_name='position',
            name='lang_en',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AddField(
            model_name='position',
            name='lang_ru',
            field=models.BooleanField(default=False, db_index=True),
        ),
    ]
