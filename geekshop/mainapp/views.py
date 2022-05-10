from django.shortcuts import render, get_object_or_404

from basketapp.models import Basket
from mainapp.models import Product, ProductCategory



def products(request, pk=None):
    title = 'Магазин : Каталог'
    links_menu = ProductCategory.objects.all().filter(is_active=True)

    basket = []
    basket_price = 0
    if request.user.is_authenticated:
        basket = Basket.objects.filter(user=request.user)
        for item in basket:
            basket_price += item.product.price * item.quantity

    if pk is not None:
        if pk == 0:
            category = {'name': 'все'}
            products = Product.objects.all().filter(is_active=True).order_by('price')
        else:
            category = get_object_or_404(ProductCategory, pk=pk)
            products = Product.objects.filter(is_active=True, category__pk=pk).order_by('price')

            context = ({
                'title': title,
                'links_menu': links_menu,
                'category': category,
                'products': products,
                'basket': basket,
                'basket_price': basket_price,
            })
            return render(request, 'mainapp/products_list.html', context)

    # import json
    # product_data = 'mainapp/static/mainapp/product.json'
    # with open(product_data, 'r', encoding='utf-8-sig') as product_data:
    #     product_data = json.load(product_data)

    same_products = Product.objects.all()[3:5]
    context = ({
        'title': title,
        'links_menu': links_menu,
        'same_products': same_products,
        'basket': basket,
        'basket_price': basket_price,
    })
    return render(request, 'mainapp/products.html', context)
