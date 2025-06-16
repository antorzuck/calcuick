from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import *
from .views import *


class StaticViewSitemap(Sitemap):

    def items(self):
        return ['category_list']

    def location(self, item):
        return reverse(item)

    def priority(self, item):
        priorities = {
            'category_list': 1.0
        }
        return priorities.get(item, 0.5)

    def changefreq(self, item):
        changefreqs = {
            'home': 'weekly'
        }
        return changefreqs.get(item, 'monthly')



class CategorySitemap(Sitemap):
    limit = 10000
    changefreq = "monthly"
    priority = 0.8

    def items(self):
        return Category.objects.all().order_by('-id')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return '/category/' + obj.slug




class CalculatorSitemap(Sitemap):
    changefreq = "weekly"
    limit = 20000
    priority = 1.0

    def items(self):
        return Calculator.objects.all().order_by('-id')

    def lastmod(self, obj):
        return obj.updated_at

    def location(self, obj):
        return '/calculator/' + obj.slug

