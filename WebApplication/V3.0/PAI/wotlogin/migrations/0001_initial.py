# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 02:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CatDisease',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('disease', models.CharField(max_length=200)),
                ('symptoms', models.CharField(max_length=200)),
                ('introduction', models.CharField(max_length=2000)),
                ('causes', models.CharField(max_length=2000)),
                ('diagnosis', models.CharField(max_length=2000)),
                ('treatment', models.CharField(max_length=2000)),
                ('recovery', models.CharField(max_length=2000)),
                ('cost', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='CatEmbeddings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.CharField(max_length=200000)),
            ],
        ),
        migrations.CreateModel(
            name='CatNce_bias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.CharField(max_length=200000)),
            ],
        ),
        migrations.CreateModel(
            name='CatNce_weight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('row', models.CharField(max_length=200000)),
            ],
        ),
    ]
