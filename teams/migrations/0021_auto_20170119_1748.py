# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-19 17:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0020_remove_teammember_college_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfilemodel',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='coding_files/'),
        ),
    ]