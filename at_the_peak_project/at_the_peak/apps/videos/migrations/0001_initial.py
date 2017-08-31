# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-31 04:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('themes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('date_uploaded', models.DateTimeField()),
                ('views', models.PositiveIntegerField()),
                ('themes', models.ManyToManyField(related_name='videos', to='themes.Theme')),
            ],
        ),
    ]
