# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-04-25 08:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0026_auto_20190409_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compose_score',
            name='stu_Id',
            field=models.CharField(max_length=255),
        ),
    ]
