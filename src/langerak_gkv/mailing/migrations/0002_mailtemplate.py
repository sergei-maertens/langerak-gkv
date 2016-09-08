# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MailTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('template_type', models.CharField(unique=True, max_length=50, verbose_name='type', choices=[(b'liturgy', 'Liturgy')])),
                ('subject', models.CharField(max_length=255, verbose_name='subject')),
                ('body', models.TextField(help_text='Add the body with {{variable}} placeholders', verbose_name='body')),
            ],
            options={
                'verbose_name': 'mail template',
                'verbose_name_plural': 'mail templates',
            },
        ),
    ]
