# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-19 18:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mcqs', '0006_auto_20170119_1727'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='choice',
            name='points',
        ),
        migrations.AddField(
            model_name='question',
            name='points',
            field=models.IntegerField(default=1),
        ),
    ]
