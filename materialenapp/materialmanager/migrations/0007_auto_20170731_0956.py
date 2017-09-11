# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-31 09:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('materialmanager', '0006_delivery_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='delivery',
            options={'verbose_name_plural': 'deliveries'},
        ),
        migrations.AddField(
            model_name='delivery',
            name='photo',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
