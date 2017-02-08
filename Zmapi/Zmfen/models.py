from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class message(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class ZmScore(models.Model):
    openid = models.CharField(max_length=30)
    certno = models.CharField(max_length=20)
    score = models.IntegerField()
    #uuidfield = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    managerid = models.ManyToManyField('CustsomManager')



class ZmOpenId(models.Model):
    openid = models.CharField(max_length=30)
    name = models.CharField(max_length=20)
    certno = models.CharField(max_length=20)

    createdata = models.DateTimeField('createdate',auto_now=True)


class Bank(models.Model):
    name = models.CharField(max_length=40)
    createdata = models.DateTimeField()



class CustsomManager(User):
    managerid = models.CharField(max_length=5)
    managerbank = models.ForeignKey('Bank')