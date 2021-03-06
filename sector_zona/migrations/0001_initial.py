# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-13 16:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Estado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Municipio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sector_zona.Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Parroquia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=1000)),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sector_zona.Municipio')),
            ],
        ),
    ]
