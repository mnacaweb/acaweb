# -*- coding: utf-8 -*-


from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('acamar_web', '0008_auto_20180816_1445'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='anchor',
            field=models.CharField(help_text='Appends the value only after the internal or external link. Do <em>not</em> include a preceding "#" symbol.', max_length=255, verbose_name='Anchor', blank=True),
        ),
    ]
