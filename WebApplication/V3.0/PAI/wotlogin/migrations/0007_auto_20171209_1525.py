# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 20:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wotlogin', '0006_auto_20171209_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='petevent',
            name='action',
            field=models.CharField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='petevent',
            name='eventtype',
            field=models.CharField(max_length=10000, null=True),
        ),
    ]
