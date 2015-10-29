# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotespage', '0005_apiuser'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='apiuser',
            options={'verbose_name': 'API user'},
        ),
        migrations.AlterField(
            model_name='apiuser',
            name='api_key',
            field=models.CharField(unique=True, max_length=64, verbose_name=b'API key'),
            preserve_default=True,
        ),
    ]
