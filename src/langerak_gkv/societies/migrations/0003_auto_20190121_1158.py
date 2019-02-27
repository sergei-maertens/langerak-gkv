# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('societies', '0002_auto_20151220_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='societyplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='societies_societyplugin', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
