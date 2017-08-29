# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-08-24 13:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Functions', '0006_auto_20170822_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='compsem1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('sem', models.CharField(max_length=200)),
                ('branch', models.CharField(max_length=200)),
                ('main_file', models.FileField(max_length=200, upload_to=b'')),
                ('code', models.CharField(max_length=200)),
            ],
        ),
    ]
