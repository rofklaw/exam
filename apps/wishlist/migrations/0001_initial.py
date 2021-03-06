# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-24 17:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logreg', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='logreg.User')),
            ],
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='wishlist.Item')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users', to='logreg.User')),
            ],
        ),
    ]
