# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-15 07:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bu',
            name='Parent_Company',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='repo.Company'),
        ),
    ]
