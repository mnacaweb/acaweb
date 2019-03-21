# -*- coding: utf-8 -*-


from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0013_teammember_linkedin'),
    ]

    operations = [
        migrations.AddField(
            model_name='thanksbanner',
            name='link',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='Link', blank=True, to='acamar_web.Link', null=True),
        ),
    ]
