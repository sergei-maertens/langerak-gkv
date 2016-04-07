# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20151220_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='external_code',
            field=models.CharField(max_length=10, null=True, verbose_name='external code', blank=True),
        ),
    ]
