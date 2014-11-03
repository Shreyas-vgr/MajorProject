# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('song_name', models.CharField(max_length=100)),
                ('artist', models.CharField(max_length=100)),
                ('album', models.CharField(max_length=100)),
                ('duration', models.FloatField(default=0)),
                ('rating', models.IntegerField(default=2)),
                ('genre', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
