# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 20:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wotlogin', '0005_auto_20171209_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='PetEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discription', models.CharField(max_length=10000, null=True)),
                ('date', models.DateTimeField(null=True)),
                ('addedinfo', models.CharField(max_length=10000, null=True)),
                ('potentialinfo', models.CharField(max_length=10000, null=True)),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wotlogin.Pet')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currentpet', models.IntegerField()),
                ('currentevent', models.IntegerField()),
            ],
        ),
        migrations.RemoveField(
            model_name='petdisease',
            name='pet',
        ),
        migrations.DeleteModel(
            name='PetDisease',
        ),
    ]
