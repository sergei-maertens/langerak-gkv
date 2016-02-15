# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20160215_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='family',
            name='address',
            field=models.CharField(help_text='Street name and number.', max_length=255, verbose_name='street', blank=True),
        ),
        migrations.AddField(
            model_name='family',
            name='city',
            field=models.CharField(max_length=100, verbose_name='city', blank=True),
        ),
        migrations.AddField(
            model_name='family',
            name='postal_code',
            field=models.CharField(default='', max_length=10, verbose_name='postal code'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='family',
            unique_together=set([('address', 'postal_code')]),
        ),
    ]
