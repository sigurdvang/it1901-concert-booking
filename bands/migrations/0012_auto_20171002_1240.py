# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-02 12:40
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bands', '0011_concert_light_tech'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='sound_tech',
            field=models.ManyToManyField(related_name='sound_tech', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='concert',
            name='light_tech',
            field=models.ManyToManyField(related_name='light_tech', to=settings.AUTH_USER_MODEL),
        ),
    ]