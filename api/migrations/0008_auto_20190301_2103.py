# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-03-01 13:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20190301_2103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursedetail',
            name='recommend',
            field=models.ManyToManyField(blank=True, to='api.FreeCourse'),
        ),
    ]
