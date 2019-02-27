# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djchoices.choices


class Migration(migrations.Migration):

    dependencies = [
        ('liturgies', '0004_auto_20161016_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mailrecipient',
            name='function',
            field=models.CharField(blank=True, max_length=50, choices=[(b'0preacher', 'predikant (predikant@langerak.gkv.nl)'), (b'koster', 'koster (koster@langerak.gkv.nl)'), (b'2beamist', 'beamist (beamist@langerak.gkv.nl)'), (b'1organist', 'organist (organist@langerak.gkv.nl)'), (b'biblegroup', 'bible group (bijbelleesgroep@langerak.gkv.nl)'), (b'preach_creation', 'preach creation (preekvoorziening@langerak.gkv.nl)')], validators=[djchoices.choices.ChoicesValidator({b'0preacher': 'predikant (predikant@langerak.gkv.nl)', b'2beamist': 'beamist (beamist@langerak.gkv.nl)', b'preach_creation': 'preach creation (preekvoorziening@langerak.gkv.nl)', b'1organist': 'organist (organist@langerak.gkv.nl)', b'koster': 'koster (koster@langerak.gkv.nl)', b'biblegroup': 'bible group (bijbelleesgroep@langerak.gkv.nl)'})]),
        ),
    ]
