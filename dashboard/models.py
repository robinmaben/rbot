from django.db import models
from django.utils import timezone


class CrawledResource(models.Model):
    name = models.CharField(max_length=50, null=False)
    url = models.CharField(max_length=256, null=False)
    last_crawled = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return '{} ({})'.format(self.name, self.url)


class CrawledPage(CrawledResource):
    is_careers_page = models.BooleanField(default=False)
    is_using_widget = models.BooleanField(default=False)
    is_paying_customer = models.BooleanField(default=False)


class CrawledSite(CrawledResource):
    careers_page = models.ForeignKey(CrawledPage)
    domain_name = models.CharField(max_length=50, null=True)


class CrawlStartPoint(CrawledResource):
    is_active = models.BooleanField(default=True)
