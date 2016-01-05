# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_delete_userinfo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=16)),
                ('number', models.IntegerField()),
                ('password', models.CharField(max_length=8)),
                ('fuclty', models.CharField(max_length=10, choices=[('システム工学群', 'システム工学群'), ('環境理工学群', '環境理工学群'), ('情報学群', '情報学群'), ('マネジメント学部', 'マネジメント学部')])),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
