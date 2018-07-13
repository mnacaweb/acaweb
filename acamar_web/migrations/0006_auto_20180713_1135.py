# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import acamar_web.fields
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('acamar_web', '0005_reviewpanel'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=254, verbose_name='Author')),
                ('text', models.TextField(verbose_name='Text')),
                ('image', filer.fields.image.FilerImageField(related_name='reviews_image', on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', blank=True, to=settings.FILER_IMAGE_MODEL, null=True)),
                ('logo', filer.fields.image.FilerImageField(related_name='reviews_logo', on_delete=django.db.models.deletion.PROTECT, verbose_name='Logo', blank=True, to=settings.FILER_IMAGE_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.AlterField(
            model_name='mainbanner',
            name='background_image',
            field=filer.fields.image.FilerImageField(related_name='main_banners_image', blank=True, to=settings.FILER_IMAGE_MODEL, help_text='Fallback for background video', null=True, verbose_name='Background image'),
        ),
        migrations.AlterField(
            model_name='mainbanner',
            name='background_video',
            field=acamar_web.fields.FilerVideoField(related_name='main_banners_video', verbose_name='Background video', blank=True, to='acamar_web.FilerVideo', null=True),
        ),
        migrations.AlterField(
            model_name='workelipsecolumn',
            name='image',
            field=filer.fields.image.FilerImageField(related_name='work_elipse_columns', on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL),
        ),
    ]
