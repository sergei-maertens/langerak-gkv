# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import cms.models.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cms', '0012_auto_20150607_2207'),
    ]

    operations = [
        migrations.CreateModel(
            name='Society',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('content', cms.models.fields.PlaceholderField(slotname=b'content', editable=False, to='cms.Placeholder', null=True)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
            options={
                'verbose_name': 'society',
                'verbose_name_plural': 'societies',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SocietyPlugin',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('page_link', cms.models.fields.PageField(blank=True, to='cms.Page', help_text='Page to link to', null=True, verbose_name='page')),
                ('society', models.ForeignKey(to='societies.Society')),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
