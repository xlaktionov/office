from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'Магазин мебели Home'

    }
    return render(request, 'main/index.html', context)

def about(request):
    context = {
        'title': 'Home - о нас',
        'content': 'О нас',
        'text_on_page': 'Текст о нашей компании с мебелью'

    }
    return render(request, 'main/about.html', context)