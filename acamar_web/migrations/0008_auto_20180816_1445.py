# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0007_auto_20180731_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseenrollformmodel',
            name='email_button',
        ),
        migrations.AddField(
            model_name='courseenrollformmodel',
            name='cv_picker_label',
            field=models.CharField(default='Vybrat soubor', max_length=254, verbose_name='CV - choose file label'),
            preserve_default=False,
        ),
    ]
