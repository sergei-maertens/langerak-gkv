# Generated by Django 2.1.15 on 2021-01-30 17:04

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="SiteConfig",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "gtm_code",
                    models.CharField(
                        blank=True,
                        help_text="Typically looks like 'GTM-XXXX'. Supplying this installs Google Tag Manager.",
                        max_length=50,
                        verbose_name="Google Tag Manager code",
                    ),
                ),
                (
                    "analytics_code",
                    models.CharField(
                        blank=True,
                        help_text="Typically looks like 'UA-XXXXX-Y'. Supplying this installs Google Analytics.",
                        max_length=50,
                        verbose_name="Google Analytics code",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
