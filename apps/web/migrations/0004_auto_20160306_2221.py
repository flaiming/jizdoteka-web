# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-06 22:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20160223_2303'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='journeywaypoints',
            unique_together=set([]),
        ),
    ]
