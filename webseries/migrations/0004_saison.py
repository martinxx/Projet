# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-25 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webseries', '0003_auto_20161024_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Saison',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saison_identifiant', models.IntegerField(default=0)),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webseries.Serie')),
            ],
        ),
    ]
