# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-31 13:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webseries', '0002_serie'),
    ]

    operations = [
        migrations.CreateModel(
            name='Season',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season_text', models.CharField(default='Noname', max_length=200)),
                ('serie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='webseries.Serie')),
            ],
        ),
    ]
