# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-15 08:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0003_auto_20180115_0751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='pageid',
            new_name='Company_Id',
        ),
    ]