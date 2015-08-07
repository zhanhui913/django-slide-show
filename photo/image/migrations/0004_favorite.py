# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0003_auto_20150805_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('image', models.ForeignKey(related_name='favorites', primary_key=True, serialize=False, to='image.Image')),
                ('order', models.IntegerField(null=True, blank=True)),
            ],
        ),
    ]
