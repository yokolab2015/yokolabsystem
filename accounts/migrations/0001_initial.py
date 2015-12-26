# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('username', models.CharField(max_length=16)),
                ('number', models.IntegerField()),
                ('password', models.CharField(max_length=8)),
                ('fuclty', models.CharField(choices=[('SSE', 'システム工学群'), ('EST', '環境理工学群'), ('SOI', '情報学群'), ('MNG', 'マネジメント学部')], max_length=3)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
