# Generated by Django 2.1.12 on 2019-11-09 16:33

from django.db import migrations
from django.db.models import F


def set_username_from_email(apps, _):
    User = apps.get_model("users.User")
    qs = User.objects.filter(username="")
    qs.update(username=F("email"))


class Migration(migrations.Migration):
    dependencies = [("users", "0001_initial")]

    operations = [
        migrations.RunPython(set_username_from_email, migrations.RunPython.noop)
    ]
