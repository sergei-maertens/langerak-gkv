# Generated by Django 2.2.17 on 2021-01-31 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="siteconfig",
            name="kerkdienst_gemist",
            field=models.URLField(blank=True, verbose_name="'kerkdienst gemist' link"),
        ),
        migrations.AddField(
            model_name="siteconfig",
            name="youtube_channel",
            field=models.URLField(blank=True, verbose_name="youtube kanaal"),
        ),
    ]
