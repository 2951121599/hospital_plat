# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-04-08 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptom',
            name='symptom_name',
            field=models.CharField(default='', max_length=30, verbose_name='症状'),
        ),
    ]
