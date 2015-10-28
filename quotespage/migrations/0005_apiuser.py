# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quotespage', '0004_quote_votes'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('api_key', models.CharField(max_length=64)),
                ('key_expires', models.DateField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
