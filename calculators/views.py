from django.shortcuts import render, get_object_or_404
from .models import Category, Calculator


def category_list(request):
    categories = Category.objects.all()
    return render(request, 'base.html', {'categories': categories})

def calculator_list(request, slug):
    category = get_object_or_404(Category, name=slug)
    calculators = category.calculators.all()
    return render(request, 'calculators/calculator_list.html', {'category': category, 'calculators': calculators})




def calculator_detail(request, slug):
    calculator = get_object_or_404(Calculator, slug=slug)

    match calculator.slug:
        case 'linear-congruence':
            return render(request, 'math/linear-congruence.html')
        case 'stokes-theorem-calculator':
            return render(request, 'math/stokes-theorem-calculator.html')
        case 'hessian-matrix-calculator':
            return render(request, 'math/hessian-matrix.html')
        case 'circle-packing-calculator':
            return render(request, 'math/circle-packing.html')
        case 'nonagon-area-calculator':
            return render(request, 'math/nonago.html')
        case 'tangent-plane-calculator':
            return render(request, 'math/tanget.html')
        case 'cost-function-calculator':
            return render(request, 'math/cost.html')
        case 'sum-of-squared-errors-calculator':
            return render(request, 'math/sse.html')
        case _:
            return render(request, 'math/default.html')
