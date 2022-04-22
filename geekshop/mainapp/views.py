from django.shortcuts import render
import json

# Create your views here.

links_main_menu = [
    {'href': 'index', 'name': 'домой'},
    {'href': 'products', 'name': 'продукты'},
    {'href': 'contacts', 'name': 'контакты'},
]

links_menu = [
    {'href': 'products', 'name': 'все'},
    {'href': 'products', 'name': 'дом'},
    {'href': 'products', 'name': 'офис'},
    {'href': 'products', 'name': 'модерн'},
    {'href': 'products', 'name': 'классика'},
]

product_data = 'mainapp/static/mainapp/product.json'
with open(product_data, 'r', encoding='utf-8') as product_data:
    product_data = json.load(product_data)


context = {
    'links_main_menu': links_main_menu,
    'links_menu': links_menu,
    "product_data": product_data,
}


def products(request):
    return render(request, 'mainapp/products.html', context)

