# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-22 02:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercise', '0010_choice_grade_fillin_grade'),
    ]

    operations = [
        migrations.CreateModel(
            name='total_grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_name', models.CharField(default='\u9009\u62e9\u9898', max_length=255)),
                ('grade', models.FloatField(default=1.0)),
            ],
            options={
                'verbose_name': '\u603b\u533a\u5206\u5ea6',
                'verbose_name_plural': '\u603b\u533a\u5206\u5ea6',
            },
        ),
        migrations.DeleteModel(
            name='choice_grade',
        ),
        migrations.DeleteModel(
            name='fillin_grade',
        ),
    ]
