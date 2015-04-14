from __future__ import unicode_literals

from django.db import models


class Category(models.Model):
    cat_id = models.IntegerField(primary_key=True)
    cat_parent = models.OneToOneField('self', null=True, db_column='cat_parent')
    cat_name = models.CharField(max_length=150)
    description = models.TextField()
    color = models.CharField(max_length=10, blank=True)
    bgcolor = models.CharField(max_length=10, blank=True)
    options = models.IntegerField(blank=True, null=True)
    level = models.CharField(max_length=255, blank=True)
    published = models.IntegerField(blank=True, null=True)
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lang_jcalpro_categories'

    def __unicode__(self):
        return self.cat_name


class Event(models.Model):
    extid = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    contact = models.TextField()
    url = models.CharField(max_length=100)
    email = models.CharField(max_length=120)
    picture = models.CharField(max_length=100)
    category = models.ForeignKey(Category, null=True, db_column='cat')
    day = models.IntegerField()
    month = models.IntegerField()
    year = models.IntegerField()
    approved = models.IntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    published = models.IntegerField(blank=True, null=True)
    checked_out = models.IntegerField()
    checked_out_time = models.DateTimeField()

    preekvan = models.TextField(blank=True)
    bijbelgedeelte = models.TextField(blank=True)
    hoofdstuk = models.TextField(blank=True)
    vers = models.TextField(blank=True)
    thema = models.TextField(blank=True)
    geluid = models.TextField(blank=True)  # file field

    liturgiebord = models.TextField(blank=True)  # liturgy

    beamist = models.TextField(blank=True)
    organist = models.TextField(blank=True)

    class Meta:
        managed = False
        db_table = 'lang_jcalpro_events'
