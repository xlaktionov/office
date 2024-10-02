from django.shortcuts import render
from goods.models import Categories

# Create your views here.
def index(request):
    categories = Categories.objects.all()
    context = {
        'title': 'Home',
        'content': 'Магазин мебели Home',
        'categories': categories,

    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - о нас',
        'content': 'О нас',
        'text_on_page': 'Текст о нашей компании с мебелью'

    }
    return render(request, 'main/about.html', context)