# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-29 11:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0011_auto_20160328_2014'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teamcodinganswer',
            old_name='answer_text',
            new_name='output_text',
        ),
    ]
