# Generated by Django 4.2.9 on 2025-01-19 13:52

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("societies", "0003_alter_societyplugin_cmsplugin_ptr"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="societyplugin",
            name="cmsplugin_ptr",
        ),
        migrations.RemoveField(
            model_name="societyplugin",
            name="page_link",
        ),
        migrations.RemoveField(
            model_name="societyplugin",
            name="society",
        ),
        migrations.DeleteModel(
            name="Society",
        ),
        migrations.DeleteModel(
            name="SocietyPlugin",
        ),
    ]
