# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20160303_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name=b'cropping',
            field=image_cropping.fields.ImageRatioField(b'picture', '400x400', hide_image_field=False, size_warning=True, allow_fullsize=False, free_crop=False, adapt_rotation=False, help_text=None, verbose_name='cropping'),
        ),
    ]
