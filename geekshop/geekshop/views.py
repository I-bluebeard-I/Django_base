from django.shortcuts import render
from mainapp.models import Product


context = {}

def index(request):
    products = Product.objects.all()[:4]
    context.update({
        'title': 'Магазин : Главная',
        'products': products,
    })
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    context.update({
        'title': 'Магазин : Контакты'
    })
    return render(request, 'geekshop/contact.html', context)
