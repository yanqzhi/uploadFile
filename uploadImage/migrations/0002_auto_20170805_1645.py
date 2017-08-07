# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-05 16:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploadImage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='media/')),
                ('thumbnail', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
