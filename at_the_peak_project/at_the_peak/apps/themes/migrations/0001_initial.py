# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-31 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60, unique=True)),
                ('pontuation_in_all_videos', models.DecimalField(blank=True, decimal_places=12, max_digits=20, null=True)),
                ('pontuation_in_recents_videos', models.DecimalField(blank=True, decimal_places=12, max_digits=20, null=True)),
            ],
        ),
    ]