from django.shortcuts import render, get_object_or_404
from .models import Category, Calculator


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'base.html', {'categories': categories})

def calculator_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    calculators = category.calculators.all()
    return render(request, 'calculators/calculator_list.html', {'category': category, 'calculators': calculators})




def calculator_detail(request, slug):
    calculator = get_object_or_404(Calculator, slug=slug)
    return render(request, f'math/{calculator.template}', context={'c':calculator})
