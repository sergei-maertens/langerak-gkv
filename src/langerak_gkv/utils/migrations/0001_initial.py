# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'URLConfMenuEntry'
        db.create_table(u'utils_urlconfmenuentry', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('app_name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('namespace', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('order', self.gf('django.db.models.fields.PositiveSmallIntegerField')(default=0)),
        ))
        db.send_create_signal(u'utils', ['URLConfMenuEntry'])


    def backwards(self, orm):
        # Deleting model 'URLConfMenuEntry'
        db.delete_table(u'utils_urlconfmenuentry')


    models = {
        u'utils.urlconfmenuentry': {
            'Meta': {'object_name': 'URLConfMenuEntry'},
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'namespace': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['utils']