# -*- coding: utf-8 -*-


from django.db import migrations, models


def run(apps, schema_editor):
    TeamMember = apps.get_model("acamar_web", "TeamMember")
    for member in TeamMember.objects.all():
        member.name_cs = member.name
        member.name_en = member.name
        member.save()


class Migration(migrations.Migration):

    dependencies = [("acamar_web", "0014_thanksbanner_link")]

    operations = [
        migrations.AddField(
            model_name="teammember",
            name="name_cs",
            field=models.CharField(max_length=254, null=True, verbose_name="Name"),
        ),
        migrations.AddField(
            model_name="teammember",
            name="name_en",
            field=models.CharField(max_length=254, null=True, verbose_name="Name"),
        ),
        migrations.AddField(
            model_name="teammember",
            name="name_ru",
            field=models.CharField(max_length=254, null=True, verbose_name="Name"),
        ),
        migrations.RunPython(run, reverse_code=lambda x, y: None),
    ]
