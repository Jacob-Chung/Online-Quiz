# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-04-16 08:08
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0023_auto_20190416_1553'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='pic',
            field=models.CharField(default=datetime.datetime(2019, 4, 16, 8, 8, 12, 582000, tzinfo=utc), max_length=256),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$24000$uiUtXxOHPCbn$outnnd3oRUxkJrDid3CZMgRcHYdXQ2TX6Hx3lo9oHZY=', max_length=256),
        ),
    ]
