# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import filer.fields.image
import acamar_web.fields
import djangocms_text_ckeditor.fields
from django.conf import settings
import django.db.models.deletion
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0010_auto_20180414_2058'),
        ('cms', '0020_old_tree_cleanup'),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
        ('acamar_api', '0001_squashed2'),
    ]

    operations = [
        migrations.CreateModel(
            name='AcaFriendCard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_acafriendcard', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('author', models.CharField(max_length=254, verbose_name='Author')),
                ('author_position', models.CharField(max_length=254, verbose_name='Author position')),
                ('text', models.TextField(verbose_name='Text')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='AcaFriendPanel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_acafriendpanel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
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
        migrations.CreateModel(
            name='BubbleCard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_bubblecard', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('text', models.TextField(verbose_name='Text')),
                ('bubble_highlight', models.CharField(max_length=254, verbose_name='Bubble highlight')),
                ('bubble_text', models.CharField(max_length=254, verbose_name='Bubble text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='BubblePanel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_bubblepanel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
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
                'verbose_name': 'Purpose option',
                'verbose_name_plural': 'Purpose options',
            },
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
        migrations.CreateModel(
            name='ContactPerson',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_contactperson', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=254, verbose_name='Sub-title', blank=True)),
                ('person_name', models.CharField(max_length=254, verbose_name='Person name')),
                ('person_title', models.CharField(max_length=254, verbose_name='Person title')),
                ('person_phone', models.CharField(max_length=254, verbose_name='Person phone', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_contactus', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CourseBasicInfo',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_coursebasicinfo', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CourseBasicInfoCard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_coursebasicinfocard', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CourseBonusCard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_coursebonuscard', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('text', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CourseBonusPanel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_coursebonuspanel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CourseGenericRegistration',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_coursegenericregistration', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('text', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CourseLector',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_courselector', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('person_name', models.CharField(max_length=254, verbose_name='Person name')),
                ('person_title', models.CharField(max_length=254, verbose_name='Person title')),
                ('text', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Text')),
                ('person_image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Person image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CoursePanel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_coursepanel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=254, verbose_name='Sub-title', blank=True)),
                ('template', models.CharField(default='', max_length=20, verbose_name='Template', blank=True, choices=[('', 'Default'), ('_alternative', 'Alternative with background')])),
                ('text', models.TextField(verbose_name='Text', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CoursePanelItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Course', to='acamar_api.Course')),
                ('course_panel', models.ForeignKey(related_name='items', to='acamar_web.CoursePanel')),
            ],
            options={
                'verbose_name': 'Course',
                'verbose_name_plural': 'Courses',
            },
        ),
        migrations.CreateModel(
            name='CourseProgram',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_courseprogram', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=254, verbose_name='Sub-title', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CourseProgramItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=254, verbose_name='Text')),
                ('parent', models.ForeignKey(related_name='items', to='acamar_web.CourseProgram')),
            ],
        ),
        migrations.CreateModel(
            name='CourseTermList',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_coursetermlist', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=254, verbose_name='Sub-title', blank=True)),
                ('additional_registration', models.BooleanField(default=False, verbose_name='Additional registration')),
                ('additional_title', models.CharField(max_length=254, verbose_name='Additional registration - title', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='CourseTermListAdditional',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=254, verbose_name='Address', blank=True)),
                ('description', models.CharField(max_length=254, verbose_name='Description', blank=True)),
                ('parent', models.ForeignKey(related_name='additional_items', to='acamar_web.CourseTermList')),
            ],
            options={
                'verbose_name': 'Additional registration - item',
                'verbose_name_plural': 'Additional registration - items',
            },
        ),
        migrations.CreateModel(
            name='CreateTeam',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_createteam', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Sub-title', blank=True)),
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
                ('subtitle', models.CharField(max_length=254, verbose_name='Sub-title', blank=True)),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
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
            name='GraphCard',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_graphcard', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='GraphCardText',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=254, verbose_name='Text')),
                ('parent', models.ForeignKey(related_name='texts', to='acamar_web.GraphCard')),
            ],
            options={
                'verbose_name': 'Graph card text',
                'verbose_name_plural': 'Graph card texts',
            },
        ),
        migrations.CreateModel(
            name='GraphSection',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_graphsection', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.CharField(max_length=255, verbose_name='Link text')),
                ('external_link', models.URLField(help_text='Provide a valid URL to an external website.', max_length=2040, verbose_name='External link', blank=True)),
                ('mailto', models.EmailField(max_length=255, verbose_name='Email address', blank=True)),
                ('phone', models.CharField(max_length=255, verbose_name='Phone', blank=True)),
                ('target', models.CharField(blank=True, max_length=255, verbose_name='Target', choices=[('_blank', 'Open in new window'), ('_self', 'Open in same window'), ('_parent', 'Delegate to parent'), ('_top', 'Delegate to top')])),
                ('internal_link', cms.models.fields.PageField(blank=True, to='cms.Page', help_text='If provided, overrides the external link.', null=True, verbose_name='Internal link')),
            ],
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
                ('button', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Button', blank=True, to='acamar_web.Link', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='MainBanner',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_mainbanner', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('template', models.CharField(default='default', max_length=100, verbose_name='Template', choices=[('default', 'Default'), ('for_candidates', 'For candidates'), ('for_companies', 'For companies'), ('we_are', 'We are'), ('course', 'Course'), ('contact', 'Contact'), ('detail', 'Detail'), ('a-card', 'A-card')])),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Sub-title', blank=True)),
                ('background_image', filer.fields.image.FilerImageField(related_name='main_banners_image', blank=True, to=settings.FILER_IMAGE_MODEL, help_text='Fallback for background video', null=True, verbose_name='Background image')),
                ('background_video', acamar_web.fields.FilerVideoField(related_name='main_banners_video', verbose_name='Background video', blank=True, to='acamar_web.FilerVideo', null=True)),
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
                ('theme', models.CharField(blank=True, max_length=30, verbose_name='Theme', choices=[('', 'Black'), ('looking-for-gray', 'Gray')])),
                ('button', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Button', blank=True, to='acamar_web.Link', null=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
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
        migrations.CreateModel(
            name='PartnersModel',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_partnersmodel', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.CharField(max_length=254, verbose_name='Sub-title')),
                ('text', models.TextField(verbose_name='Text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
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
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_quote', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Sub-title')),
                ('text', djangocms_text_ckeditor.fields.HTMLField(verbose_name='Text')),
                ('author', models.CharField(max_length=254, verbose_name='Author')),
                ('author_title', models.CharField(max_length=254, verbose_name='Author - title')),
                ('author_image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Author - image', to=settings.FILER_IMAGE_MODEL)),
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
                ('author_cs', models.CharField(max_length=254, null=True, verbose_name='Author')),
                ('author_en', models.CharField(max_length=254, null=True, verbose_name='Author')),
                ('author_ru', models.CharField(max_length=254, null=True, verbose_name='Author')),
                ('text', models.TextField(verbose_name='Text')),
                ('text_cs', models.TextField(null=True, verbose_name='Text')),
                ('text_en', models.TextField(null=True, verbose_name='Text')),
                ('text_ru', models.TextField(null=True, verbose_name='Text')),
                ('show', models.BooleanField(default=True, db_index=True, verbose_name='Show')),
                ('image', filer.fields.image.FilerImageField(related_name='reviews_image', on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', blank=True, to=settings.FILER_IMAGE_MODEL, null=True)),
                ('logo', filer.fields.image.FilerImageField(related_name='reviews_logo', on_delete=django.db.models.deletion.PROTECT, verbose_name='Logo', blank=True, to=settings.FILER_IMAGE_MODEL, null=True)),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
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
                ('nickname_cs', models.CharField(max_length=254, null=True, verbose_name='Position / Nickname')),
                ('nickname_en', models.CharField(max_length=254, null=True, verbose_name='Position / Nickname')),
                ('nickname_ru', models.CharField(max_length=254, null=True, verbose_name='Position / Nickname')),
                ('text', models.TextField(verbose_name='Text')),
                ('text_cs', models.TextField(null=True, verbose_name='Text')),
                ('text_en', models.TextField(null=True, verbose_name='Text')),
                ('text_ru', models.TextField(null=True, verbose_name='Text')),
                ('order', models.PositiveIntegerField(default=0, editable=False, db_index=True)),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL)),
            ],
            options={
                'ordering': ['order'],
                'verbose_name': 'Team member',
                'verbose_name_plural': 'Team members',
            },
        ),
        migrations.CreateModel(
            name='Timeline',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_timeline', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Sub-title', blank=True)),
                ('title_after', models.CharField(max_length=254, verbose_name='Title after', blank=True)),
                ('subtitle_after', models.TextField(verbose_name='Sub-title after', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='TimelineItem',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='acamar_web_timelineitem', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=254, verbose_name='Title', blank=True)),
                ('text', models.TextField(verbose_name='Text', blank=True)),
                ('image', filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', blank=True, to=settings.FILER_IMAGE_MODEL, null=True)),
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
                ('title', models.CharField(max_length=254, verbose_name='Title')),
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
        migrations.AddField(
            model_name='graphsection',
            name='button',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Button', blank=True, to='acamar_web.Link', null=True),
        ),
        migrations.AddField(
            model_name='coursetermlist',
            name='button',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Registration button', to='acamar_web.Link'),
        ),
        migrations.AddField(
            model_name='coursepanel',
            name='button',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Button', blank=True, to='acamar_web.Link', null=True),
        ),
        migrations.AddField(
            model_name='coursegenericregistration',
            name='button',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Button', to='acamar_web.Link'),
        ),
        migrations.AddField(
            model_name='contactus',
            name='additional_link',
            field=models.ForeignKey(related_name='contact_us_additional_set', on_delete=django.db.models.deletion.PROTECT, verbose_name='Additional link', blank=True, to='acamar_web.Link', null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='button',
            field=models.ForeignKey(related_name='contact_us_button_set', on_delete=django.db.models.deletion.PROTECT, verbose_name='Button', blank=True, to='acamar_web.Link', null=True),
        ),
        migrations.AddField(
            model_name='contactperson',
            name='button',
            field=models.ForeignKey(related_name='contact_person_button_set', on_delete=django.db.models.deletion.PROTECT, verbose_name='Button', blank=True, to='acamar_web.Link', null=True),
        ),
        migrations.AddField(
            model_name='contactperson',
            name='image',
            field=filer.fields.image.FilerImageField(on_delete=django.db.models.deletion.PROTECT, verbose_name='Image', to=settings.FILER_IMAGE_MODEL),
        ),
        migrations.AddField(
            model_name='contactperson',
            name='more',
            field=models.ForeignKey(related_name='contact_person_more_set', on_delete=django.db.models.deletion.PROTECT, verbose_name='More link', blank=True, to='acamar_web.Link', null=True),
        ),
    ]
