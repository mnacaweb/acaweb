# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0010_teamgrid_more_button'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseenrollformmodel',
            name='email_label',
            field=models.CharField(default='V\xe1\u0161 email', max_length=254, verbose_name='Email label'),
            preserve_default=False,
        ),
    ]
