# Generated by Django 2.2.28 on 2022-04-27 13:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0005_remove_user_member_type"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="family",
            unique_together={("name", "address", "postal_code")},
        ),
    ]