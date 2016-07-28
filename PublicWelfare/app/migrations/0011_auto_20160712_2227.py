# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 14:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20160711_2318'),
    ]

    operations = [
        migrations.CreateModel(
            name='VolunteerSkill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='volunteer',
            name='skill',
        ),
        migrations.AddField(
            model_name='volunteer',
            name='skills',
            field=models.ManyToManyField(to='app.VolunteerSkill'),
        ),
    ]
