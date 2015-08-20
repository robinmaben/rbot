# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='crawledsite',
            name='domain_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='crawledpage',
            name='is_careers_page',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='crawledpage',
            name='is_paying_customer',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='crawledpage',
            name='is_using_widget',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='crawledresource',
            name='last_crawled',
            field=models.DateTimeField(default=datetime.datetime(2015, 8, 20, 6, 57, 30, 728471, tzinfo=utc)),
        ),
    ]
