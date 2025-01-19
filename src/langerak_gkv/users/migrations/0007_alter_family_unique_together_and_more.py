# Generated by Django 4.2.9 on 2025-01-19 15:44

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0006_auto_20220427_1542"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="family",
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name="relationtype",
            name="reverse",
        ),
        migrations.RemoveField(
            model_name="userrelation",
            name="relation_type",
        ),
        migrations.RemoveField(
            model_name="userrelation",
            name="user1",
        ),
        migrations.RemoveField(
            model_name="userrelation",
            name="user2",
        ),
        migrations.AlterModelManagers(
            name="user",
            managers=[
                ("objects", django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name="user",
            name="about_me",
        ),
        migrations.RemoveField(
            model_name="user",
            name="address",
        ),
        migrations.RemoveField(
            model_name="user",
            name="birthdate",
        ),
        migrations.RemoveField(
            model_name="user",
            name="city",
        ),
        migrations.RemoveField(
            model_name="user",
            name="cropping",
        ),
        migrations.RemoveField(
            model_name="user",
            name="district",
        ),
        migrations.RemoveField(
            model_name="user",
            name="district_function",
        ),
        migrations.RemoveField(
            model_name="user",
            name="exclude_in_queries",
        ),
        migrations.RemoveField(
            model_name="user",
            name="external_code",
        ),
        migrations.RemoveField(
            model_name="user",
            name="family",
        ),
        migrations.RemoveField(
            model_name="user",
            name="mobile",
        ),
        migrations.RemoveField(
            model_name="user",
            name="phone",
        ),
        migrations.RemoveField(
            model_name="user",
            name="picture",
        ),
        migrations.RemoveField(
            model_name="user",
            name="postal_code",
        ),
        migrations.RemoveField(
            model_name="user",
            name="relations",
        ),
        migrations.RemoveField(
            model_name="user",
            name="sex",
        ),
        migrations.AlterField(
            model_name="user",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="last name"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(
                error_messages={"unique": "A user with that username already exists."},
                help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
                max_length=150,
                unique=True,
                validators=[django.contrib.auth.validators.UnicodeUsernameValidator()],
                verbose_name="username",
            ),
        ),
        migrations.DeleteModel(
            name="District",
        ),
        migrations.DeleteModel(
            name="DistrictFunction",
        ),
        migrations.DeleteModel(
            name="Family",
        ),
        migrations.DeleteModel(
            name="RelationType",
        ),
        migrations.DeleteModel(
            name="UserRelation",
        ),
    ]
