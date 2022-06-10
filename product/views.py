from django.shortcuts import render
from .models import *

# Create your views here.

def base_view(request):
    if request.method == "GET":
        categories = Category.objects.all()
        return render(request, "base.html", {'categories': categories})

    elif request.method == "POST":
        category = request.POST.get('button', None)
        category_name = Category.objects.get(category=category)
        products = Product.objects.filter(category=category_name)
        return render(request, "base.html", {'products': products})


def order_view(request, product):
    if request.method =='GET':
        return render(request, "order.html", {'product':product})

    elif request.method == "POST":
        quantity = request.POST.get('quantity', None)
        address = request.POST.get('address', None)

        ordered = UserOrder.objects.create(address=address, num=quantity)













