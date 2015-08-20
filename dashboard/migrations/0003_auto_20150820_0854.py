# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20150820_0658'),
    ]

    operations = [
        migrations.CreateModel(
            name='CrawlStartPoint',
            fields=[
                ('crawledresource_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='dashboard.CrawledResource')),
                ('is_active', models.BooleanField(default=True)),
            ],
            bases=('dashboard.crawledresource',),
        ),
        migrations.AlterField(
            model_name='crawledresource',
            name='last_crawled',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='crawledsite',
            name='domain_name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
