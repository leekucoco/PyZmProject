# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-08 07:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Zmfen', '0003_auto_20170208_0638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zmopenid',
            name='createdata',
            field=models.DateTimeField(auto_now=True, verbose_name='createdate'),
        ),
    ]
