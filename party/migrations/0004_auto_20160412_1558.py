# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-12 15:58
from __future__ import unicode_literals

from django.db import migrations, models
import party.models


class Migration(migrations.Migration):

    dependencies = [
        ('party', '0003_auto_20160412_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='venue',
            name='pic',
            field=models.ImageField(upload_to=party.models.upload_location_main),
        ),
    ]
