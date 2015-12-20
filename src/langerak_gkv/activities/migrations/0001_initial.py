# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import autoslug.fields
import cms.models.fields
import filer.fields.image


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('liturgies', '0001_initial'),
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('slug', autoslug.fields.AutoSlugField(populate_from=b'name', unique=True, null=True, editable=False)),
                ('start_date', models.DateField(verbose_name='start date')),
                ('end_date', models.DateField(verbose_name='end date')),
                ('start_time', models.TimeField(null=True, verbose_name='start time', blank=True)),
                ('end_time', models.TimeField(null=True, verbose_name='end time', blank=True)),
                ('location', models.CharField(max_length=255, verbose_name='location', blank=True)),
                ('description', models.TextField(verbose_name='short description/intro')),
                ('show_on_homepage', models.BooleanField(default=False, help_text='If checked, this activity can appear on the homepage.')),
                ('url', models.URLField(verbose_name='external url', blank=True)),
                ('fb_event_id', models.CharField(max_length=50, verbose_name='facebook event id', blank=True)),
                ('content', cms.models.fields.PlaceholderField(slotname=b'content', editable=False, to='cms.Placeholder', null=True)),
                ('image', filer.fields.image.FilerImageField(blank=True, to='filer.Image', null=True)),
            ],
            options={
                'ordering': ['start_date', 'start_time', 'end_date', 'end_time'],
                'verbose_name': 'activity',
                'verbose_name_plural': 'activities',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='IntendedPublic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
            ],
            options={
                'verbose_name': 'intended public',
                'verbose_name_plural': 'intended public',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='activity',
            name='intended_public',
            field=models.ForeignKey(blank=True, to='activities.IntendedPublic', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='liturgy',
            field=models.ForeignKey(editable=False, to='liturgies.Liturgy', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='activity',
            name='type',
            field=models.ForeignKey(to='activities.ActivityType'),
            preserve_default=True,
        ),
    ]
