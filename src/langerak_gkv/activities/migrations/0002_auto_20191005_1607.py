# Generated by Django 2.1.12 on 2019-10-05 14:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [("activities", "0001_initial"), ("liturgies", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="activity",
            name="liturgy",
            field=models.ForeignKey(
                editable=False,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="liturgies.Liturgy",
            ),
        ),
        migrations.AddField(
            model_name="activity",
            name="type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="activities.ActivityType",
            ),
        ),
    ]
