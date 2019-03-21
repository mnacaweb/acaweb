# -*- coding: utf-8 -*-


from django.db import migrations, models
import filer.fields.image
import django.db.models.deletion
import djangocms_text_ckeditor.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('acamar_web', '0001_squashed2'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartnersItem',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_partnersitem', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.CASCADE)),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('text', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Text')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.RemoveField(
            model_name='partnersmodel',
            name='subtitle',
        ),
        migrations.RemoveField(
            model_name='partnersmodel',
            name='text',
        ),
    ]
