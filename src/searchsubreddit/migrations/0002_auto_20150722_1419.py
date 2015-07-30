# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchsubreddit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchbox',
            name='searchbar',
            field=models.CharField(default=b"e.g. '/r/funny'", max_length=120, blank=True),
        ),
    ]
