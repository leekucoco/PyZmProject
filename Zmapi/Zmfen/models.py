from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class message(models.Model):
#     username = models.CharField(max_length=30)
#     password = models.CharField(max_length=30)
#

class ZmScore(models.Model):
    openid = models.CharField(max_length=30)
    certno = models.CharField(max_length=20)
    score = models.IntegerField()
    managerid = models.ManyToManyField('CustsomerManager')
    createdate = models.DateTimeField('scorecreatedate', auto_now=True)
    def __unicode__(self):
        return self.score

class ZmOpenId(models.Model):
    openid = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    certno = models.CharField(max_length=20)
    createdate = models.DateTimeField('openidcreatedate',auto_now=True)
    def __unicode__(self):
        return self.openid

class Bank(models.Model):
    name = models.CharField(max_length=40)
    createdate = models.DateTimeField('bankcreatedate', auto_now=True)
    def __unicode__(self):
        return self.name

class CustsomerManager(models.Model):
    user = models.OneToOneField(User)
    managerid = models.CharField(max_length=6)
    managerbank = models.ForeignKey('Bank')
    def __unicode__(self):
        return self.managerid