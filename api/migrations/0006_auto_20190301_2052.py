# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-03-01 12:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190301_2052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='level',
            field=models.SmallIntegerField(choices=[(0, '铜牌'), (1, '银牌'), (2, '金牌')]),
        ),
    ]
