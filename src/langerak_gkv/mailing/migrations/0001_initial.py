# Generated by Django 2.1.12 on 2019-10-05 14:07

from django.db import migrations, models
import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Mail",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("to", models.TextField()),
                ("cc", models.TextField(blank=True)),
                ("bcc", models.TextField(blank=True)),
                ("subject", models.CharField(max_length=255)),
                ("body", models.TextField()),
                ("sent", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "email",
                "verbose_name_plural": "emails",
                "ordering": ("-pk",),
            },
        ),
        migrations.CreateModel(
            name="MailTemplate",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "template_type",
                    models.CharField(
                        choices=[("liturgy", "Liturgy")],
                        max_length=50,
                        unique=True,
                        verbose_name="type",
                    ),
                ),
                ("subject", models.CharField(max_length=255, verbose_name="subject")),
                (
                    "body",
                    djangocms_text_ckeditor.fields.HTMLField(
                        help_text="Add the body with {{variable}} placeholders",
                        verbose_name="body",
                    ),
                ),
            ],
            options={
                "verbose_name": "mail template",
                "verbose_name_plural": "mail templates",
            },
        ),
    ]
