# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0002_mailtemplate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailtemplate',
            name='body',
            field=djangocms_text_ckeditor.fields.HTMLField(help_text='Add the body with {{variable}} placeholders', verbose_name='body'),
        ),
    ]
