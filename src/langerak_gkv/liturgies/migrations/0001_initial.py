# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import djchoices.choices


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Liturgy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField(verbose_name='date')),
                ('preacher', models.CharField(max_length=100, verbose_name='preacher')),
                ('preach_author', models.CharField(max_length=100, verbose_name='preach author')),
                ('main_section', models.CharField(max_length=50, verbose_name='main section', blank=True)),
                ('main_chapter', models.CharField(max_length=50, verbose_name='main chapter', blank=True)),
                ('main_verse', models.CharField(max_length=50, verbose_name='main verse', blank=True)),
                ('service_theme', models.CharField(max_length=255, verbose_name='service theme', blank=True)),
                ('liturgy', models.TextField(verbose_name='liturgy')),
                ('audiofile', models.FileField(upload_to=b'liturgies/audio', verbose_name='audiofile', blank=True)),
                ('beamist', models.CharField(max_length=50, verbose_name='beamist', blank=True)),
                ('organist', models.CharField(max_length=50, verbose_name='organist', blank=True)),
                ('collection_goal1', models.CharField(max_length=50, verbose_name='collection goal 1', blank=True)),
                ('collection_goal2', models.CharField(max_length=50, verbose_name='collection goal 2', blank=True)),
                ('collection_goal3', models.CharField(max_length=50, verbose_name='collection goal 3', blank=True)),
                ('extra_information', models.TextField(verbose_name='extra information', blank=True)),
                ('internal_remarks', models.TextField(verbose_name='remarks (internal)', blank=True)),
            ],
            options={
                'ordering': ['-date'],
                'verbose_name': 'liturgy',
                'verbose_name_plural': 'liturgies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MailRecipient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email', models.EmailField(max_length=254, blank=True)),
                ('function', models.CharField(blank=True, max_length=10, choices=[(b'0preacher', 'preacher (predikant@koningskerk.nu)'), (b'1organist', 'organist (organist@koningskerk.nu)'), (b'2beamist', 'beamist (beamist@koningskerk.nu)'), (b'koster', 'koster (koster@koningskerk.nu)'), (b'3other', 'other')], validators=[djchoices.choices.ChoicesValidator({b'0preacher': 'preacher (predikant@koningskerk.nu)', b'koster': 'koster (koster@koningskerk.nu)', b'2beamist': 'beamist (beamist@koningskerk.nu)', b'3other': 'other', b'1organist': 'organist (organist@koningskerk.nu)'})])),
                ('is_sent', models.BooleanField(default=False)),
                ('liturgy', models.ForeignKey(verbose_name='liturgy', to='liturgies.Liturgy')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, max_length=100, null=True)),
            ],
            options={
                'ordering': ['function'],
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='service name')),
                ('time', models.TimeField(verbose_name='service time')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='liturgy',
            name='service',
            field=models.ForeignKey(verbose_name='service', to='liturgies.Service'),
            preserve_default=True,
        ),
    ]
