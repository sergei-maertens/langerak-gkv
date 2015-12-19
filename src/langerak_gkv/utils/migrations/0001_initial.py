# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URLConfMenuEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('app_name', models.CharField(max_length=50, verbose_name='app name')),
                ('name', models.CharField(max_length=50, verbose_name='url name')),
                ('display_name', models.CharField(max_length=100, verbose_name='display name')),
                ('namespace', models.CharField(max_length=50, verbose_name='url namespace', blank=True)),
                ('order', models.PositiveSmallIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'urlconf menu entry',
                'verbose_name_plural': 'urlconf menu entries',
            },
            bases=(models.Model,),
        ),
    ]
