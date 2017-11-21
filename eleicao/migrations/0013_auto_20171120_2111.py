# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-21 00:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eleicao', '0012_auto_20171120_2044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votacao',
            name='token',
        ),
        migrations.AddField(
            model_name='eleitor',
            name='token',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='eleicao.Token'),
            preserve_default=False,
        ),
    ]