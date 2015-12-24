# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_auto_20151220_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepagepagelink',
            name='description',
            field=djangocms_text_ckeditor.fields.HTMLField(help_text='Displayed below the title', verbose_name='description'),
        ),
    ]
