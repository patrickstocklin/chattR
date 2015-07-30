# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('searchsubreddit', '0003_auto_20150722_1448'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchbox',
            old_name='meh',
            new_name='searchBar',
        ),
    ]
