# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('docmng', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('sid', models.DateTimeField(verbose_name='date published')),
                ('passwd', models.CharField(max_length=8)),
                ('faculty', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.AlterField(
            model_name='document',
            name='path',
            field=models.FileField(upload_to=None),
        ),
    ]
