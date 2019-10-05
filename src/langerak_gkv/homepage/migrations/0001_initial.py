# Generated by Django 2.1.12 on 2019-10-05 14:07

import cms.models.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import djangocms_text_ckeditor.fields
import filer.fields.image


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("cms", "0022_auto_20180620_1551"),
        migrations.swappable_dependency(settings.FILER_IMAGE_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="CharFieldPlugin",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="homepage_charfieldplugin",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                ("content", models.CharField(max_length=255, verbose_name="text")),
            ],
            options={"abstract": False},
            bases=("cms.cmsplugin",),
        ),
        migrations.CreateModel(
            name="HomepagePageLink",
            fields=[
                (
                    "cmsplugin_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        related_name="homepage_homepagepagelink",
                        serialize=False,
                        to="cms.CMSPlugin",
                    ),
                ),
                ("title", models.CharField(max_length=50, verbose_name="title")),
                (
                    "description",
                    djangocms_text_ckeditor.fields.HTMLField(
                        help_text="Displayed below the title",
                        verbose_name="description",
                    ),
                ),
                (
                    "enable_sharing",
                    models.BooleanField(
                        default=True, verbose_name="enable social sharing"
                    ),
                ),
                (
                    "image",
                    filer.fields.image.FilerImageField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.FILER_IMAGE_MODEL,
                        verbose_name="image",
                    ),
                ),
                (
                    "page_link",
                    cms.models.fields.PageField(
                        blank=True,
                        help_text="Page to link to",
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="cms.Page",
                        verbose_name="page",
                    ),
                ),
            ],
            options={"abstract": False},
            bases=("cms.cmsplugin",),
        ),
        migrations.CreateModel(
            name="PrayerOnDemand",
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
                ("name", models.CharField(max_length=100, verbose_name="name")),
                ("email", models.EmailField(max_length=254, verbose_name="email")),
                ("body", models.TextField(verbose_name="What should we pray for?")),
                ("replied", models.BooleanField(default=False, verbose_name="replied")),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("modified", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "prayer on demand",
                "verbose_name_plural": "prayer on demands",
            },
        ),
    ]
