# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-31 08:47
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils import timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='added',
            field=models.DateTimeField(auto_now_add=True, default=timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='report',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]