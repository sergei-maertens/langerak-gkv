# Generated by Django 2.1.12 on 2019-10-05 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("liturgies", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name="mailrecipient",
            name="user",
            field=models.ForeignKey(
                blank=True,
                max_length=100,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="liturgy",
            name="other_churches",
            field=models.ManyToManyField(
                blank=True, to="liturgies.Church", verbose_name="other churches"
            ),
        ),
        migrations.AddField(
            model_name="liturgy",
            name="service",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="liturgies.Service",
                verbose_name="service",
            ),
        ),
    ]