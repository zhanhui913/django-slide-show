# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image', '0002_favorite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='favorite',
            name='image',
        ),
        migrations.AddField(
            model_name='image',
            name='is_fav',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
