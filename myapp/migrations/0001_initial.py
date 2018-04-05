# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-05 10:47
from __future__ import unicode_literals

from django.db import migrations, models
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GenQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poll', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('oneliner', models.CharField(max_length=200)),
                ('votes', jsonfield.fields.JSONField()),
            ],
        ),
    ]