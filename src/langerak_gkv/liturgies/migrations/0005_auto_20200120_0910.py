# Generated by Django 2.1.13 on 2020-01-20 08:10

from django.db import migrations

import djangocms_text_ckeditor.fields


class Migration(migrations.Migration):
    dependencies = [("liturgies", "0004_liturgy_download")]

    operations = [
        migrations.AlterField(
            model_name="liturgy",
            name="liturgy",
            field=djangocms_text_ckeditor.fields.HTMLField(
                blank=True, verbose_name="liturgy"
            ),
        )
    ]
