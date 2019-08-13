# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-08-12 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommonData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('commondata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abstractapp.CommonData')),
                ('salesamt', models.IntegerField()),
            ],
            bases=('abstractapp.commondata',),
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('commondata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abstractapp.CommonData')),
                ('salesamt', models.IntegerField()),
            ],
            bases=('abstractapp.commondata',),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('commondata_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='abstractapp.CommonData')),
                ('marks', models.IntegerField()),
            ],
            bases=('abstractapp.commondata',),
        ),
    ]