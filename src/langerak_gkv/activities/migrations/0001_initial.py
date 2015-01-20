# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Activity'
        db.create_table(u'activities_activity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('start_date', self.gf('django.db.models.fields.DateField')()),
            ('end_date', self.gf('django.db.models.fields.DateField')()),
            ('start_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('end_time', self.gf('django.db.models.fields.TimeField')(null=True, blank=True)),
            ('intended_public', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['activities.IntendedPublic'], null=True, blank=True)),
            ('type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['activities.ActivityType'])),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('content', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['cms.Placeholder'], null=True)),
            ('url', self.gf('django.db.models.fields.URLField')(max_length=200, blank=True)),
            ('liturgy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['liturgies.Liturgy'], null=True)),
            ('fb_event_id', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
        ))
        db.send_create_signal(u'activities', ['Activity'])

        # Adding model 'IntendedPublic'
        db.create_table(u'activities_intendedpublic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'activities', ['IntendedPublic'])

        # Adding model 'ActivityType'
        db.create_table(u'activities_activitytype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'activities', ['ActivityType'])


    def backwards(self, orm):
        # Deleting model 'Activity'
        db.delete_table(u'activities_activity')

        # Deleting model 'IntendedPublic'
        db.delete_table(u'activities_intendedpublic')

        # Deleting model 'ActivityType'
        db.delete_table(u'activities_activitytype')


    models = {
        u'activities.activity': {
            'Meta': {'ordering': "['start_date', 'start_time', 'end_date', 'end_time']", 'object_name': 'Activity'},
            'content': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['cms.Placeholder']", 'null': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'end_date': ('django.db.models.fields.DateField', [], {}),
            'end_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'fb_event_id': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'intended_public': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['activities.IntendedPublic']", 'null': 'True', 'blank': 'True'}),
            'liturgy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['liturgies.Liturgy']", 'null': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'start_time': ('django.db.models.fields.TimeField', [], {'null': 'True', 'blank': 'True'}),
            'type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['activities.ActivityType']"}),
            'url': ('django.db.models.fields.URLField', [], {'max_length': '200', 'blank': 'True'})
        },
        u'activities.activitytype': {
            'Meta': {'object_name': 'ActivityType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'activities.intendedpublic': {
            'Meta': {'object_name': 'IntendedPublic'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'cms.placeholder': {
            'Meta': {'object_name': 'Placeholder'},
            'default_width': ('django.db.models.fields.PositiveSmallIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'slot': ('django.db.models.fields.CharField', [], {'max_length': '255', 'db_index': 'True'})
        },
        u'liturgies.liturgy': {
            'Meta': {'ordering': "['date']", 'object_name': 'Liturgy'},
            'audiofile': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'beamist': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'collection_goal1': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'collection_goal2': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'collection_goal3': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateTimeField', [], {}),
            'extra_information': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'liturgy': ('django.db.models.fields.TextField', [], {}),
            'main_section': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'main_verse': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'organist': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'preach_author': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'preacher': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'service': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['liturgies.Service']"}),
            'service_theme': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'})
        },
        u'liturgies.service': {
            'Meta': {'object_name': 'Service'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        }
    }

    complete_apps = ['activities']