from django.contrib import admin
from .models import Category, Calculator, CalculatorField

admin.site.register(Category)
admin.site.register(Calculator)
admin.site.register(CalculatorField)