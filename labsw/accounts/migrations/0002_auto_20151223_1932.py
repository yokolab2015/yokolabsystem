# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='fuclty',
            field=models.CharField(max_length=10, choices=[('システム工学群', 'システム工学群'), ('環境理工学群', '環境理工学群'), ('情報学群', '情報学群'), ('マネジメント学部', 'マネジメント学部')]),
        ),
    ]
