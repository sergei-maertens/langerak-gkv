# Generated by Django 2.1.13 on 2019-12-01 15:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations

import filer.fields.image


class Migration(migrations.Migration):
    dependencies = [("homepage", "0002_remove_homepagepagelink_enable_sharing")]

    operations = [
        migrations.AlterField(
            model_name="homepagepagelink",
            name="image",
            field=filer.fields.image.FilerImageField(
                help_text="Block image - note that only rows 1 and 3 display images. Images will be cropped to 300x300",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.FILER_IMAGE_MODEL,
                verbose_name="image",
            ),
        )
    ]
