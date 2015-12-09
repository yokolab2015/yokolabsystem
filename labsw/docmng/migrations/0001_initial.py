# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=128)),
                ('day', models.DateTimeField(verbose_name='date published')),
                ('author', models.CharField(max_length=16)),
                ('type', models.CharField(max_length=8)),
                ('format', models.CharField(max_length=8)),
                ('sid', models.CharField(max_length=8)),
                ('path', models.CharField(max_length=516)),
            ],
        ),
    ]
