# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 01:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_auto_20160706_0944'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='TeamMember',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='TeamMember', to=settings.AUTH_USER_MODEL),
        ),
    ]
