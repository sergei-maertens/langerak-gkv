# Generated by Django 2.1.13 on 2019-12-01 15:25

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [("homepage", "0001_initial")]

    operations = [
        migrations.RemoveField(model_name="homepagepagelink", name="enable_sharing")
    ]
