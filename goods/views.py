from django.shortcuts import render
from goods.models import Products
# Create your views here.

def catalog(request, category_slug):
    if category_slug == 'all':
     goods = Products.objects.all()
    else:
     goods = Products.objects.filter(category__slug=category_slug)
    context = {
        "title":'Home - Каталог',
        'goods': goods,
    }
    return render(request, 'goods/catalog.html', context)



def product(request, product_slug):
    goods = Products.objects.get(slug=product_slug)
    context = {
        'goods': goods,
    }
    return render(request, 'goods/product.html', context=context)