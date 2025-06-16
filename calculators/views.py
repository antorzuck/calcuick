from django.shortcuts import render, get_object_or_404
from .models import Category, Calculator
from django.views.decorators.cache import cache_page
from django.http import HttpResponse




@cache_page(60 * 10)
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'base.html', {'categories': categories})


@cache_page(60 * 10)
def calculator_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    calculators = category.calculators.all()
    return render(request, 'calculators/calculator_list.html', {'category': category, 'calculators': calculators})


@cache_page(60 * 10)
def calculator_detail(request, slug):
    calculator = get_object_or_404(Calculator, slug=slug)
    return render(request, f'math/{calculator.template}', context={'c':calculator})




def robots_txt(request):
    lines = [
        "User-agent: *",
        "Disallow:",
        "Sitemap: https://calcuick.com/sitemap.xml",
        "Sitemap: https://calcuick.com/sitemap-static.xml",
        "Sitemap: https://calcuick.com/sitemap-category.xml",
        "Sitemap: https://calcuick.com/sitemap-calculators.xml",
    ]
    return HttpResponse("\n".join(lines), content_type="text/plain")










