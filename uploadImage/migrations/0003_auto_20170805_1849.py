# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 18:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadImage', '0002_auto_20170805_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagefile',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
