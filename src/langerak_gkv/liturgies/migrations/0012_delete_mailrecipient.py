# Generated by Django 4.2.9 on 2025-01-19 14:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("liturgies", "0011_alter_church_options_remove_liturgy_beamist_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="MailRecipient",
        ),
    ]
