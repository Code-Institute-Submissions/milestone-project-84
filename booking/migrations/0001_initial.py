# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-07-07 11:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=50)),
                ('date', models.DateTimeField()),
                ('seat_type', models.SmallIntegerField(choices=[(1, 'Bar Stool'), (2, 'Window Seat'), (3, 'Snug'), (4, 'Table')], default=1)),
                ('reserved_start_time', models.TimeField()),
                ('reserved_end_time', models.TimeField()),
                ('status', models.SmallIntegerField(choices=[(1, 'Requested'), (2, 'Accepted'), (3, 'Denied')], default=1)),
            ],
        ),
    ]
