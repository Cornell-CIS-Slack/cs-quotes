# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('date', models.DateField()),
                ('speaker', models.CharField(max_length=100)),
                ('speaker_class', models.CharField(max_length=3, default='FAC', choices=[('FAC', 'Faculty'), ('GS', 'Graduate Student'), ('INV', 'Invited Speaker')])),
                ('quotation', models.TextField()),
                ('context', models.CharField(max_length=256, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
