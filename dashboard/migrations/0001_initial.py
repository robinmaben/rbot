# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrawledResource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('url', models.CharField(max_length=256)),
                ('last_crawled', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='CrawledPage',
            fields=[
                ('crawledresource_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='dashboard.CrawledResource')),
                ('is_careers_page', models.BooleanField()),
                ('is_using_widget', models.BooleanField()),
                ('is_paying_customer', models.BooleanField()),
            ],
            bases=('dashboard.crawledresource',),
        ),
        migrations.CreateModel(
            name='CrawledSite',
            fields=[
                ('crawledresource_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='dashboard.CrawledResource')),
                ('careers_page', models.ForeignKey(to='dashboard.CrawledPage')),
            ],
            bases=('dashboard.crawledresource',),
        ),
    ]
