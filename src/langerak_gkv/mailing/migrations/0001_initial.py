# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('to', models.TextField()),
                ('cc', models.TextField(blank=True)),
                ('bcc', models.TextField(blank=True)),
                ('subject', models.CharField(max_length=255)),
                ('body', models.TextField()),
                ('sent', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-pk',),
                'verbose_name': 'email',
                'verbose_name_plural': 'emails',
            },
            bases=(models.Model,),
        ),
    ]
