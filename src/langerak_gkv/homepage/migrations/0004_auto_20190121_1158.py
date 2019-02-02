# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0003_auto_20151224_1537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charfieldplugin',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='homepage_charfieldplugin', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
        migrations.AlterField(
            model_name='homepagepagelink',
            name='cmsplugin_ptr',
            field=models.OneToOneField(parent_link=True, related_name='homepage_homepagepagelink', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin'),
        ),
    ]
