# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2020-04-08 11:57
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=50, verbose_name='科室')),
            ],
            options={
                'verbose_name': '科室表',
                'verbose_name_plural': '科室表',
                'db_table': 'department',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='医生姓名')),
                ('skill', models.CharField(max_length=200, verbose_name='专长')),
                ('introduce', models.CharField(max_length=500, verbose_name='简介')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('department', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='patient.Department')),
            ],
            options={
                'verbose_name': '医生信息',
                'verbose_name_plural': '医生信息',
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=20, verbose_name='药品名称')),
                ('medicine_num', models.IntegerField(verbose_name='药品库存数量')),
            ],
            options={
                'verbose_name': '药品信息',
                'verbose_name_plural': '药品信息',
                'db_table': 'medicine',
            },
        ),
        migrations.CreateModel(
            name='MedicineRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=20, verbose_name='药品名称')),
                ('medicine_num', models.IntegerField(verbose_name='购药数量')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('user', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'verbose_name': '购药记录表',
                'verbose_name_plural': '购药记录表',
                'db_table': 'medicine_record',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=500, verbose_name='咨询内容')),
                ('comment', models.CharField(default='', max_length=500, verbose_name='评论内容')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('updated_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('doctor', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='patient.Doctor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.User')),
            ],
            options={
                'verbose_name': '咨询问题与回复',
                'verbose_name_plural': '咨询问题与回复',
                'db_table': 'questions',
            },
        ),
        migrations.CreateModel(
            name='Symptom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('symptom_name', models.CharField(default='暂无', max_length=30, verbose_name='症状')),
            ],
            options={
                'verbose_name': '症状表',
                'verbose_name_plural': '症状表',
                'db_table': 'symptom',
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='symptom',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='patient.Symptom'),
        ),
    ]
