# Generated by Django 2.1 on 2019-11-29 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0019_auto_20191129_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='blocklinks',
            name='link_button',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='linkbutton', to='acamar_web.Link', verbose_name='Link button'),
        ),
    ]