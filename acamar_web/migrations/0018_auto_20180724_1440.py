# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import filer.fields.image
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('acamar_web', '0017_timelineitem_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcardBenefits',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_acardbenefits', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=254, verbose_name='Sub-title')),
                ('text', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='AcardBenefitsItem',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_acardbenefitsitem', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Subtitle')),
                ('text', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Text')),
                ('icon', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Icon', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterField(
            model_name='mainbanner',
            name='template',
            field=models.CharField(default='default', max_length=100, verbose_name='Template', choices=[('default', 'Default'), ('for_candidates', 'For candidates'), ('for_companies', 'For companies'), ('we_are', 'We are'), ('course', 'Course'), ('contact', 'Contact'), ('detail', 'Detail'), ('a-card', 'A-card')]),
        ),
    ]
