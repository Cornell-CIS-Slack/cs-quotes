# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotespage', '0006_auto_20151029_1047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='speaker_class',
            field=models.CharField(default=b'FAC', max_length=3, choices=[(b'FAC', b'Faculty'), (b'GS', b'Graduate Student'), (b'INV', b'Invited Speaker'), (b'OTH', b'Other')]),
            preserve_default=True,
        ),
    ]
