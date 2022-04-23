from django.shortcuts import render
from mainapp.models import ProductCategory


context = {}

def products(request):
    links_menu = ProductCategory.objects.all()

    import json
    product_data = 'mainapp/static/mainapp/product.json'
    with open(product_data, 'r', encoding='utf-8-sig') as product_data:
        product_data = json.load(product_data)

    context.update({
        'links_menu': links_menu,
        'product_data': product_data,
        'title': 'Магазин : Каталог'
    })
    return render(request, 'mainapp/products.html', context)
