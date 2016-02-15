# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


def delete_families(apps, schema_editor):
    """
    Delete families before making schema changes
    """
    Family = apps.get_model('users', 'Family')
    User = apps.get_model('users', 'User')
    User.objects.update(family=None)
    Family.objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_external_code'),
    ]

    operations = [
        migrations.RunPython(delete_families),
    ]
