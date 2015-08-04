# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.FileField(upload_to=b'')),
                ('caption', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=2000)),
                ('upload_date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
