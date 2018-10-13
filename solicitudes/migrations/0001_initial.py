# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-13 05:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departamento', '0001_initial'),
        ('sector_zona', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solicitud',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_de_oficio', models.CharField(max_length=200)),
                ('fecha', models.DateField()),
                ('caso_planteado', models.CharField(max_length=200)),
                ('tipo_solicitud', models.CharField(choices=[('1', 'Personal'), ('2', 'Alto Riezgo'), ('3', 'Salud'), ('4', 'Institucional')], max_length=200)),
                ('estado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sector_zona.Estado')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sector_zona.Municipio')),
                ('parroquia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sector_zona.Parroquia')),
                ('remitente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='departamento.Departamento')),
            ],
        ),
    ]
