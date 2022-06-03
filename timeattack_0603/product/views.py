from django.shortcuts import render
from .models import Category, Drink


# Create your views here.
def product_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "main.html", {'categories': categories})

    elif request.method == "POST":
        name = request.POST.get('name', None)
        category = Category.objects.get(category=name)
        drinks = Drink.objects.filter(category=category)
        print(drinks)
        return render(request, 'main.html', {'drinks': drinks})



