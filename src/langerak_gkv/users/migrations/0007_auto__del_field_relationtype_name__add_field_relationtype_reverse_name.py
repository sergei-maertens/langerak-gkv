# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'RelationType.name'
        db.delete_column(u'users_relationtype', 'name')

        # Adding field 'RelationType.reverse_name_male'
        db.add_column(u'users_relationtype', 'reverse_name_male',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)

        # Adding field 'RelationType.reverse_name_female'
        db.add_column(u'users_relationtype', 'reverse_name_female',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'RelationType.name'
        db.add_column(u'users_relationtype', 'name',
                      self.gf('django.db.models.fields.CharField')(default='relation name', max_length=100),
                      keep_default=False)

        # Deleting field 'RelationType.reverse_name_male'
        db.delete_column(u'users_relationtype', 'reverse_name_male')

        # Deleting field 'RelationType.reverse_name_female'
        db.delete_column(u'users_relationtype', 'reverse_name_female')


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
        u'users.district': {
            'Meta': {'object_name': 'District'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'users.districtfunction': {
            'Meta': {'object_name': 'DistrictFunction'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'users.family': {
            'Meta': {'object_name': 'Family'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'users.relationtype': {
            'Meta': {'object_name': 'RelationType'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_child_parent': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_partner': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'name_female': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_male': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'reverse': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.RelationType']", 'null': 'True'}),
            'reverse_name_female': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'reverse_name_male': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.District']", 'null': 'True', 'blank': 'True'}),
            'district_function': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.DistrictFunction']", 'null': 'True', 'blank': 'True'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '254'}),
            'family': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.Family']", 'null': 'True', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'mobile': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'picture': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'postal_code': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'relations': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': u"orm['users.User']", 'null': 'True', 'through': u"orm['users.UserRelation']", 'blank': 'True'}),
            'sex': ('django.db.models.fields.CharField', [], {'default': "'male'", 'max_length': '10', 'blank': 'True'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"})
        },
        u'users.userrelation': {
            'Meta': {'object_name': 'UserRelation'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'relation_type': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'+'", 'to': u"orm['users.RelationType']"}),
            'user1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user1_set'", 'to': u"orm['users.User']"}),
            'user2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user2_set'", 'to': u"orm['users.User']"})
        }
    }

    complete_apps = ['users']