from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('category/<slug:slug>/', views.calculator_list, name='calculator_list'),
    path('calculator/<slug:slug>/', views.calculator_detail, name='calculator_detail'),
]