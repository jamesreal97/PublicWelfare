# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 14:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_auto_20160712_2227'),
    ]

    operations = [
        migrations.AddField(
            model_name='volunteer',
            name='comments',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='isCPC',
            field=models.BooleanField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='volunteer',
            name='photo',
            field=models.URLField(default=''),
            preserve_default=False,
        ),
    ]
