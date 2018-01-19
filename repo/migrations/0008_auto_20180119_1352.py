# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-01-19 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0007_auto_20180119_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='plstandard',
            name='AverageCustomersPerSite',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='plstandard',
            name='DA',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='plstandard',
            name='DirectCosts',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='plstandard',
            name='DirectFuelCosts',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='plstandard',
            name='EBIT',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='plstandard',
            name='EBITDA',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='plstandard',
            name='EnvironmentalAndSocialCosts',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='plstandard',
            name='IndirectCosts',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='plstandard',
            name='NetworkCosts',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='plstandard',
            name='OtherDirectCosts',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='plstandard',
            name='OtherRevenue',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='plstandard',
            name='SalesofElectricityandGas',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='plstandard',
            name='TotalOperatingCosts',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='plstandard',
            name='Volume',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='plstandard',
            name='WACOFEG',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='plstandard',
            name='TotalRevenue',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
