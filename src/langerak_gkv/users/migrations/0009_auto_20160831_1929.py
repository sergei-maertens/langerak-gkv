# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_auto_20160630_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='exclude_in_queries',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='district_function',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, verbose_name='district function', blank=True, to='users.DistrictFunction', null=True),
        ),
    ]
