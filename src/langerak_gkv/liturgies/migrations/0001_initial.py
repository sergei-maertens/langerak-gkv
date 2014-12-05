# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Liturgy'
        db.create_table(u'liturgies_liturgy', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('date', self.gf('django.db.models.fields.DateTimeField')()),
            ('service', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['liturgies.Service'])),
            ('preacher', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('preach_author', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('main_section', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('main_verse', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('service_theme', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('liturgy', self.gf('django.db.models.fields.TextField')()),
            ('audiofile', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('beamist', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('organist', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('collection_goal1', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('collection_goal2', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('collection_goal3', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('extra_information', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal(u'liturgies', ['Liturgy'])

        # Adding model 'Service'
        db.create_table(u'liturgies_service', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('time', self.gf('django.db.models.fields.TimeField')()),
        ))
        db.send_create_signal(u'liturgies', ['Service'])

        # Adding model 'MailRecipient'
        db.create_table(u'liturgies_mailrecipient', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('liturgy', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['liturgies.Liturgy'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(max_length=100, to=orm['users.User'], null=True, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=254)),
            ('function', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
            ('is_sent', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'liturgies', ['MailRecipient'])


    def backwards(self, orm):
        # Deleting model 'Liturgy'
        db.delete_table(u'liturgies_liturgy')

        # Deleting model 'Service'
        db.delete_table(u'liturgies_service')

        # Deleting model 'MailRecipient'
        db.delete_table(u'liturgies_mailrecipient')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'liturgies.liturgy': {
            'Meta': {'object_name': 'Liturgy'},
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
        u'liturgies.mailrecipient': {
            'Meta': {'ordering': "['function']", 'object_name': 'MailRecipient'},
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '254'}),
            'function': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_sent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'liturgy': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['liturgies.Liturgy']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'max_length': '100', 'to': u"orm['users.User']", 'null': 'True', 'blank': 'True'})
        },
        u'liturgies.service': {
            'Meta': {'object_name': 'Service'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'time': ('django.db.models.fields.TimeField', [], {})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        }
    }

    complete_apps = ['liturgies']