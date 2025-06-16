from django.urls import path
from . import views
from django.contrib.sitemaps.views import sitemap, index
from calculators.sitemap import *

sitemaps = {
    'static' : StaticViewSitemap,
    'category': CategorySitemap,
    'calculators': CalculatorSitemap,
}


urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<slug:slug>/', views.calculator_list, name='calculator_list'),
    path('calculator/<slug:slug>/', views.calculator_detail, name='calculator_detail'),

    path("sitemap.xml/", index, {'sitemaps': sitemaps}, name='sitemap-index'),
    path("sitemap-<section>.xml", sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path("robots.txt/", robots_txt),
]
