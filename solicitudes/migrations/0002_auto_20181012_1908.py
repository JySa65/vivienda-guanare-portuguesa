# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-12 23:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sector_zona', '0001_initial'),
        ('solicitudes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitud',
            name='estado',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sector_zona.Estado'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='municipio',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sector_zona.Municipio'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='solicitud',
            name='parroquia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='sector_zona.Parroquia'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='solicitud',
            name='remitente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.Departamento'),
        ),
    ]