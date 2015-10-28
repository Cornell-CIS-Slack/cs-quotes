# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotespage', '0003_auto_20141203_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='votes',
            field=models.SmallIntegerField(default=0),
            preserve_default=True,
        ),
    ]
