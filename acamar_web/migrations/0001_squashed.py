# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import acamar_web.fields
import cms.models.fields
import filer.fields.image
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0010_auto_20180414_2058'),
        ('cms', '0020_old_tree_cleanup'),
        ('filer', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilerVideo',
            fields=[
                ('file_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='filer.File')),
            ],
            options={
                'abstract': False,
            },
            bases=('filer.file',),
        ),
        migrations.CreateModel(
            name='MainBanner',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_mainbanner', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default='default', max_length=100, verbose_name='Template', choices=[('default', 'Default'), ('candidates', 'Candidates'), ('we_are', 'We are'), ('course', 'Course'), ('contact', 'Contact'), ('detail', 'Detail')])),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Sub-title')),
                ('background_image', filer.fields.image.FilerImageField(related_name='main_banners_image', blank=True, to=settings.FILER_IMAGE_MODEL, help_text='Fallback for background video', null=True, verbose_name='Background image')),
                ('background_video', acamar_web.fields.FilerVideoField(related_name='main_banners_video', verbose_name='Background video', blank=True, to=b'acamar_web.FilerVideo', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='MainBannerCard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_mainbannercard', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Sub-title')),
                ('button_text', models.CharField(max_length=254, verbose_name='Button text')),
                ('theme', models.CharField(blank=True, max_length=30, verbose_name='Theme', choices=[('', 'Black'), ('looking-for-gray', 'Gray')])),
                ('button_link', cms.models.fields.PageField(verbose_name='Button link', to=b'cms.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='WorkElipse',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_workelipse', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.TextField(verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='WorkElipseColumn',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('image', filer.fields.image.FilerImageField(related_name='work_elipse_columns', on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
                ('parent', models.ForeignKey(related_name='columns', to='acamar_web.WorkElipse')),
            ],
        ),
        migrations.AlterField(
            model_name='workelipse',
            name='title',
            field=models.CharField(max_length=254, verbose_name='Title'),
        ),
        migrations.CreateModel(
            name='ReviewPanel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_reviewpanel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Sub-title')),
                ('positions_pretext', models.CharField(max_length=254, verbose_name='Positions - pre-text')),
                ('positions_number', models.PositiveSmallIntegerField(verbose_name='Positions - number')),
                ('positions_posttext', models.CharField(max_length=254, verbose_name='Positions - post-text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('author', models.CharField(max_length=254, verbose_name='Author')),
                ('text', models.TextField(verbose_name='Text')),
                ('image', filer.fields.image.FilerImageField(related_name='reviews_image', on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', blank=True, to=settings.FILER_IMAGE_MODEL, null=True)),
                ('logo', filer.fields.image.FilerImageField(related_name='reviews_logo', on_delete=django.db.models.deletion.PROTECT, verbose_name='Logo', blank=True, to=settings.FILER_IMAGE_MODEL, null=True)),
                ('show', models.BooleanField(default=True, db_index=True, verbose_name='Show')),
                ('author_cs', models.CharField(max_length=254, null=True, verbose_name='Author')),
                ('author_en', models.CharField(max_length=254, null=True, verbose_name='Author')),
                ('author_ru', models.CharField(max_length=254, null=True, verbose_name='Author')),
                ('text_cs', models.TextField(null=True, verbose_name='Text')),
                ('text_en', models.TextField(null=True, verbose_name='Text')),
                ('text_ru', models.TextField(null=True, verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='CoursePanel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_coursepanel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=254, verbose_name='Sub-title')),
                ('text', models.TextField(verbose_name='Text')),
                ('button_text', models.CharField(max_length=254, verbose_name='Button text')),
                ('button_link', cms.models.fields.PageField(verbose_name='Button link', to=b'cms.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CreateTeam',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_createteam', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Sub-title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CreateTeamCard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_createteamcard', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=254, verbose_name='Sub-title')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TeamGrid',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_teamgrid', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Sub-title')),
                ('button_text', models.CharField(max_length=254, verbose_name='Button text')),
                ('limit', models.PositiveSmallIntegerField(null=True, verbose_name='Limit count', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TeamMember',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254, verbose_name='Name')),
                ('nickname', models.CharField(max_length=254, verbose_name='Position / Nickname')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Team member',
                'verbose_name_plural': 'Team members',
            },
        ),
        migrations.CreateModel(
            name='Logo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_logo', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('image', filer.fields.image.FilerImageField(related_name='teamwork_logos', on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='LogoPanel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_logopanel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('button_text', models.CharField(max_length=254, verbose_name='Button text')),
                ('button_link', cms.models.fields.PageField(verbose_name='Button link', to=b'cms.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterModelOptions(
            name='teammember',
            options={'ordering': ['order'], 'verbose_name': 'Team member', 'verbose_name_plural': 'Team members'},
        ),
        migrations.AddField(
            model_name='teammember',
            name='order',
            field=models.PositiveIntegerField(default=0, editable=False, db_index=True),
        ),
        migrations.AddField(
            model_name='teammember',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, default=7, verbose_name='Image', to=settings.FILER_IMAGE_MODEL),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ContactCard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_contactcard', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('name', models.CharField(max_length=254, verbose_name='Name')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('phone', models.CharField(max_length=20, verbose_name='Phone', blank=True)),
                ('email', models.EmailField(max_length=254, verbose_name='Email', blank=True)),
                ('linkedin', models.URLField(verbose_name='LinedIn URL', blank=True)),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ContactGrid',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_contactgrid', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AddField(
            model_name='teammember',
            name='nickname_cs',
            field=models.CharField(max_length=254, null=True, verbose_name='Position / Nickname'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='nickname_en',
            field=models.CharField(max_length=254, null=True, verbose_name='Position / Nickname'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='nickname_ru',
            field=models.CharField(max_length=254, null=True, verbose_name='Position / Nickname'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='text_cs',
            field=models.TextField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='text_en',
            field=models.TextField(null=True, verbose_name='Text'),
        ),
        migrations.AddField(
            model_name='teammember',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Text'),
        ),
        migrations.CreateModel(
            name='ContactFormModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_contactformmodel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=254, verbose_name='Sub-title')),
                ('name_label', models.CharField(max_length=254, verbose_name='Label - name')),
                ('email_label', models.CharField(max_length=254, verbose_name='Label - email')),
                ('purpose_label', models.CharField(max_length=254, verbose_name='Label - purpose')),
                ('text_label', models.CharField(max_length=254, verbose_name='Label - text')),
                ('button_text', models.CharField(max_length=254, verbose_name='Button text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ContactFormPurposeOption',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=254, verbose_name='Option name')),
                ('form', models.ForeignKey(related_name='purpose_options', editable=False, to='acamar_web.ContactFormModel')),
            ],
            options={
                'verbose_name': 'Option',
                'verbose_name_plural': 'Options',
            },
        ),
        migrations.CreateModel(
            name='Map',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_map', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.TextField(verbose_name='Title')),
                ('address', models.TextField(verbose_name='Address')),
                ('ic', models.CharField(max_length=254, verbose_name='I\u010c with label')),
                ('dic', models.CharField(max_length=254, verbose_name='DI\u010c with label')),
                ('phone', models.CharField(max_length=254, verbose_name='Phone with label')),
                ('email', models.CharField(max_length=254, verbose_name='Email with label')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.AlterModelOptions(
            name='contactformpurposeoption',
            options={'verbose_name': 'Purpose option', 'verbose_name_plural': 'Purpose options'},
        ),
        migrations.CreateModel(
            name='PositionSearch',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_positionsearch', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('search_placeholder', models.CharField(max_length=254, verbose_name='Search input placeholder')),
                ('search_button', models.CharField(max_length=254, verbose_name='Search button text')),
                ('all_pacts_text', models.CharField(default='V\u0161echny \xfavazky', max_length=254, verbose_name='All jobs text')),
                ('recruiter_text', models.CharField(default='Provedu v\xe1s n\xe1borem', max_length=254, verbose_name='Recruiter text')),
                ('recruiter_email_text', models.CharField(default='Napi\u0161te mi e-mail', max_length=254, verbose_name='Recruiter email text')),
                ('more_button_text', models.CharField(max_length=254, verbose_name='More button text')),
                ('limit', models.PositiveSmallIntegerField(null=True, verbose_name='Limit results', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
