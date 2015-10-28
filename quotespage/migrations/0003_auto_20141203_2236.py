# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django_bleach.models


class Migration(migrations.Migration):

    dependencies = [
        ('quotespage', '0002_quote_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quote',
            options={'ordering': ['-date']},
        ),
        migrations.AlterField(
            model_name='quote',
            name='quotation',
            field=django_bleach.models.BleachField(),
            preserve_default=True,
        ),
    ]
