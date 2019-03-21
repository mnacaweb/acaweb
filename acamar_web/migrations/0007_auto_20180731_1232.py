# -*- coding: utf-8 -*-


from cms.models import Page
from django.db import migrations, models
import cms.models.fields
import djangocms_text_ckeditor.fields


def get_page():
    return Page.objects.first().id


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0006_auto_20180731_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='ThanksBanner',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_thanksbanner', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.CASCADE)),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('text', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='courseenrollformmodel',
            name='thanks_page',
            field=cms.models.fields.PageField(default=get_page, verbose_name='Thanks page', to=b'cms.Page'),
            preserve_default=False,
        ),
    ]
