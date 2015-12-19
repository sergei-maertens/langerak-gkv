# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start', models.DateTimeField(verbose_name='start')),
                ('end', models.DateTimeField(verbose_name='end')),
                ('log_message', models.CharField(max_length=512, verbose_name='log_message')),
                ('paid', models.BooleanField(default=False, verbose_name='paid?')),
                ('user', models.ForeignKey(related_name='worklogentry_set', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-end', '-start'),
                'verbose_name': 'log entry',
                'verbose_name_plural': 'log entries',
            },
            bases=(models.Model,),
        ),
    ]
