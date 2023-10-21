# Generated by Django 2.2.17 on 2021-02-09 19:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("liturgies", "0008_auto_20210131_1554"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailrecipient",
            name="function",
            field=models.CharField(
                blank=True,
                choices=[
                    ("0preacher", "preacher (predikant@langerak.gkv.nl)"),
                    ("koster", "koster (koster@langerak.gkv.nl)"),
                    ("2beamist", "beamist (beamist@langerak.gkv.nl)"),
                    ("1organist", "organist (organist@langerak.gkv.nl)"),
                    ("biblegroup", "bible group (bijbelleesgroep@langerak.gkv.nl)"),
                    (
                        "preach_creation",
                        "preach creation (preekvoorziening@langerak.gkv.nl)",
                    ),
                ],
                max_length=50,
            ),
        ),
    ]
