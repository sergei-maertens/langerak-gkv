# Generated by Django 2.2.17 on 2021-01-31 14:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("liturgies", "0007_auto_20210131_1519_squashed_0008_auto_20210131_1520"),
    ]

    operations = [
        migrations.AlterField(
            model_name="liturgy",
            name="download",
            field=models.URLField(
                blank=True, help_text="Download link", verbose_name="download"
            ),
        ),
    ]
