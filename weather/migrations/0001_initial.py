# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-08-23 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forecast',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('min_temp', models.IntegerField()),
                ('max_temp', models.IntegerField()),
                ('wind_speed', models.IntegerField()),
                ('wind_direction', models.CharField(max_length=10)),
                ('rain', models.IntegerField()),
            ],
        ),
    ]