# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djchoices.choices


class Migration(migrations.Migration):

    dependencies = [
        ('liturgies', '0002_auto_20160215_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='Church',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
        ),
        migrations.AlterField(
            model_name='mailrecipient',
            name='function',
            field=models.CharField(blank=True, max_length=10, choices=[(b'0preacher', 'predikant (predikant@langerak.gkv.nl)'), (b'1organist', 'organist (organist@langerak.gkv.nl)'), (b'2beamist', 'beamist (beamist@langerak.gkv.nl)'), (b'koster', 'organist (koster@langerak.gkv.nl)'), (b'3other', 'other')], validators=[djchoices.choices.ChoicesValidator({b'0preacher': 'predikant (predikant@langerak.gkv.nl)', b'koster': 'organist (koster@langerak.gkv.nl)', b'2beamist': 'beamist (beamist@langerak.gkv.nl)', b'3other': 'other', b'1organist': 'organist (organist@langerak.gkv.nl)'})]),
        ),
        migrations.AddField(
            model_name='liturgy',
            name='other_churches',
            field=models.ManyToManyField(to='liturgies.Church', verbose_name='other churches', blank=True),
        ),
    ]
