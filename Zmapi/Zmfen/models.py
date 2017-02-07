from __future__ import unicode_literals

from django.db import models

import uuid
# Create your models here.

class message(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)


class ZmScore(models.Model):
    openid = models.CharField(max_length=30)
    certno = models.CharField(max_length=20)
    score = models.IntegerField()
    uuidfield = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)