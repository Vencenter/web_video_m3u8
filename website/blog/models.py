# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals
from django.db import models


class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField( max_length=40)  # Field name made lowercase.
    age = models.IntegerField()  # Field name made lowercase.
    address = models.CharField(max_length=100)  # Field name made lowercase.
    inttime = models.DateTimeField()
    area = models.CharField(max_length=40)

    class Meta:
        db_table = 'member'
    def __unicode__(self):
        return self.name


class Data(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=40, blank=True, null=True)
    inttime = models.DateTimeField()

    class Meta:
        db_table = 'data'
    def __unicode__(self):
        return self.name


class Mitao(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    pic = models.CharField(max_length=200, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        db_table = 'mitao'
    def __unicode__(self):
        return str(self.title+ "_" + str(self.id))
