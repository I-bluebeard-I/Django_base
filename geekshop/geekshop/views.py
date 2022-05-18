from django.shortcuts import render

from basketapp.models import Basket
from mainapp.models import Product


def index(request):
    products = Product.objects.all()[:4]

    basket = []
    basket_price = 0
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        for item in basket:
            basket_price += item.product.price * item.quantity

    context = ({
        'title': 'Магазин : Главная',
        'products': products,
        'basket': basket,
        'basket_price': basket_price,
    })
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    basket = []
    basket_price = 0
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        for item in basket:
            basket_price += item.product.price * item.quantity

    context = ({
        'title': 'Магазин : Контакты',
        'basket': basket,
        'basket_price': basket_price,
    })
    return render(request, 'geekshop/contact.html', context)
