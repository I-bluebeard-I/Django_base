from django.shortcuts import render

# Create your views here.

links_main_menu = [
    {'href': 'index', 'name': 'домой'},
    {'href': 'products', 'name': 'продукты'},
    {'href': 'contacts', 'name': 'контакты'},
]

context = {
    'links_main_menu': links_main_menu
}

def index(request):
    return render(request, 'geekshop/index.html', context)


def contacts(request):
    return render(request, 'geekshop/contact.html', context)
