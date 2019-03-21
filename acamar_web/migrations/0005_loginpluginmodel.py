# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('acamar_web', '0004_courseenrollformmodel_selected_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='LoginPluginModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_loginpluginmodel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin', on_delete=models.CASCADE)),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=254, verbose_name='Sub-title', blank=True)),
                ('username_label', models.CharField(max_length=254, verbose_name='Username label')),
                ('password_label', models.CharField(max_length=254, verbose_name='Password label')),
                ('button_text', models.CharField(max_length=254, verbose_name='Button text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
