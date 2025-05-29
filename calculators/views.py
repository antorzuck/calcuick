from django.shortcuts import render, get_object_or_404
from .models import Category, Calculator

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'calculators/category_list.html', {'categories': categories})

def calculator_list(request, slug):
    category = get_object_or_404(Category, name=slug)
    calculators = category.calculators.all()
    return render(request, 'calculators/calculator_list.html', {'category': category, 'calculators': calculators})

def modinv(a, m):
    # Extended Euclidean Algorithm for modular inverse
    g, x, y = extended_gcd(a, m)
    if g != 1:
        return None  # No solution
    return x % m

def extended_gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = extended_gcd(b % a, a)
        return (g, x - (b // a) * y, y)

def calculator_detail(request, slug):
    calculator = get_object_or_404(Calculator, slug=slug)
    fields = calculator.fields.all()
    result = None
    error = None

    if request.method == 'POST':
        input_data = {f.name: float(request.POST.get(f.name)) for f in fields if request.POST.get(f.name)}

        print("POST REQUESTED")
        
        if calculator.slug == 'linear-congruence':
            print("YES MATCHED SLUG")
            a = int(input_data.get('a'))
            b = int(input_data.get('b'))
            m = int(input_data.get('m'))

            inv = modinv(a, m)
            if inv is None:
                error = "No solution exists (a and m are not coprime)."
            else:
                x = (inv * b) % m
                result = f"x ≡ {x} mod {m}"

        # You can add more calculators here with elif

        print(result)

    return render(request, 'calculators/calculator_detail.html', {
        'calculator': calculator,
        'fields': fields,
        'result': result,
        'error': error,
    })
