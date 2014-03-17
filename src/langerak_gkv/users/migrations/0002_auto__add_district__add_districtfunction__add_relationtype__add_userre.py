# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'District'
        db.create_table(u'users_district', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'users', ['District'])

        # Adding model 'DistrictFunction'
        db.create_table(u'users_districtfunction', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
        ))
        db.send_create_signal(u'users', ['DistrictFunction'])

        # Adding model 'RelationType'
        db.create_table(u'users_relationtype', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name_male', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_female', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_reverse_male', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('name_reverse_female', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'users', ['RelationType'])

        # Adding model 'UserRelation'
        db.create_table(u'users_userrelation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('user1', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user1_set', to=orm['users.User'])),
            ('user2', self.gf('django.db.models.fields.related.ForeignKey')(related_name='user2_set', to=orm['users.User'])),
            ('relation_type', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.RelationType'])),
        ))
        db.send_create_signal(u'users', ['UserRelation'])

        # Adding model 'Family'
        db.create_table(u'users_family', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'users', ['Family'])

        # Adding field 'User.sex'
        db.add_column(u'users_user', 'sex',
                      self.gf('django.db.models.fields.CharField')(default='male', max_length=10, blank=True),
                      keep_default=False)

        # Adding field 'User.address'
        db.add_column(u'users_user', 'address',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=255, blank=True),
                      keep_default=False)

        # Adding field 'User.postal_code'
        db.add_column(u'users_user', 'postal_code',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=10, blank=True),
                      keep_default=False)

        # Adding field 'User.city'
        db.add_column(u'users_user', 'city',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=100, blank=True),
                      keep_default=False)

        # Adding field 'User.phone'
        db.add_column(u'users_user', 'phone',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)

        # Adding field 'User.mobile'
        db.add_column(u'users_user', 'mobile',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)

        # Adding field 'User.birthdate'
        db.add_column(u'users_user', 'birthdate',
                      self.gf('django.db.models.fields.DateField')(null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.district'
        db.add_column(u'users_user', 'district',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.District'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.disctrict_function'
        db.add_column(u'users_user', 'disctrict_function',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.DistrictFunction'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.family'
        db.add_column(u'users_user', 'family',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['users.Family'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'User.picture'
        db.add_column(u'users_user', 'picture',
                      self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'District'
        db.delete_table(u'users_district')

        # Deleting model 'DistrictFunction'
        db.delete_table(u'users_districtfunction')

        # Deleting model 'RelationType'
        db.delete_table(u'users_relationtype')

        # Deleting model 'UserRelation'
        db.delete_table(u'users_userrelation')

        # Deleting model 'Family'
        db.delete_table(u'users_family')

        # Deleting field 'User.sex'
        db.delete_column(u'users_user', 'sex')

        # Deleting field 'User.address'
        db.delete_column(u'users_user', 'address')

        # Deleting field 'User.postal_code'
        db.delete_column(u'users_user', 'postal_code')

        # Deleting field 'User.city'
        db.delete_column(u'users_user', 'city')

        # Deleting field 'User.phone'
        db.delete_column(u'users_user', 'phone')

        # Deleting field 'User.mobile'
        db.delete_column(u'users_user', 'mobile')

        # Deleting field 'User.birthdate'
        db.delete_column(u'users_user', 'birthdate')

        # Deleting field 'User.district'
        db.delete_column(u'users_user', 'district_id')

        # Deleting field 'User.disctrict_function'
        db.delete_column(u'users_user', 'disctrict_function_id')

        # Deleting field 'User.family'
        db.delete_column(u'users_user', 'family_id')

        # Deleting field 'User.picture'
        db.delete_column(u'users_user', 'picture')


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
            'name_female': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_male': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_reverse_female': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_reverse_male': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'users.user': {
            'Meta': {'object_name': 'User'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'birthdate': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'disctrict_function': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.DistrictFunction']", 'null': 'True', 'blank': 'True'}),
            'district': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.District']", 'null': 'True', 'blank': 'True'}),
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
            'relation_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['users.RelationType']"}),
            'user1': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user1_set'", 'to': u"orm['users.User']"}),
            'user2': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'user2_set'", 'to': u"orm['users.User']"})
        }
    }

    complete_apps = ['users']