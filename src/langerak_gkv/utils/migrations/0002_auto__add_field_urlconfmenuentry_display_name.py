# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'URLConfMenuEntry.display_name'
        db.add_column(u'utils_urlconfmenuentry', 'display_name',
                      self.gf('django.db.models.fields.CharField')(default='FIXME', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'URLConfMenuEntry.display_name'
        db.delete_column(u'utils_urlconfmenuentry', 'display_name')


    models = {
        u'utils.urlconfmenuentry': {
            'Meta': {'object_name': 'URLConfMenuEntry'},
            'app_name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'display_name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'namespace': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'order': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['utils']