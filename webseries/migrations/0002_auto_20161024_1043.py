# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 10:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webseries', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serie',
            old_name='choice_text',
            new_name='serie_text',
        ),
    ]
