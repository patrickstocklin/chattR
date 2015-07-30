# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchsubreddit', '0004_auto_20150722_1453'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchbox',
            old_name='searchBar',
            new_name='Peek',
        ),
    ]
