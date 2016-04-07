# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djchoices.choices


class Migration(migrations.Migration):

    dependencies = [
        ('liturgies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailrecipient',
            name='function',
            field=models.CharField(blank=True, max_length=10, choices=[(b'0preacher', 'predikant (predikant@koningskerk.nu)'), (b'1organist', 'organist (organist@koningskerk.nu)'), (b'2beamist', 'beamist (beamist@koningskerk.nu)'), (b'koster', 'organist (koster@koningskerk.nu)'), (b'3other', 'other')], validators=[djchoices.choices.ChoicesValidator({b'0preacher': 'predikant (predikant@koningskerk.nu)', b'koster': 'organist (koster@koningskerk.nu)', b'2beamist': 'beamist (beamist@koningskerk.nu)', b'3other': 'other', b'1organist': 'organist (organist@koningskerk.nu)'})]),
        ),
    ]
