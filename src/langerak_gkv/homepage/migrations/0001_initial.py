# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import filer.fields.image
import cms.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('filer', '0002_auto_20150606_2003'),
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='CharFieldPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('content', models.CharField(max_length=255, verbose_name='text')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='HomepagePageLink',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('description', models.TextField(help_text='Displayed below the title', verbose_name='description')),
                ('enable_sharing', models.BooleanField(default=True, verbose_name='enable social sharing')),
                ('image', filer.fields.image.FilerImageField(verbose_name='image', to='filer.Image')),
                ('page_link', cms.models.fields.PageField(blank=True, to='cms.Page', help_text='Page to link to', null=True, verbose_name='page')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
        migrations.CreateModel(
            name='PrayerOnDemand',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100, verbose_name='name')),
                ('email', models.EmailField(max_length=75, verbose_name='email')),
                ('body', models.TextField(verbose_name='What should we pray for?')),
                ('replied', models.BooleanField(default=False, verbose_name='replied')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'prayer on demand',
                'verbose_name_plural': 'prayer on demands',
            },
            bases=(models.Model,),
        ),
    ]
