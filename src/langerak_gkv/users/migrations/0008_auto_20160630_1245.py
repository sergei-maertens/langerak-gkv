# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20160407_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userrelation',
            name='user1',
            field=models.ForeignKey(related_name='related_users', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='userrelation',
            name='user2',
            field=models.ForeignKey(related_name='reverse_related_users', to=settings.AUTH_USER_MODEL),
        ),
    ]
