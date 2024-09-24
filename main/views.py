from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'title': 'Home',
        'content': 'Главная страница - Home'

    }
    return render(request, 'main/index.html', context)

def about(request):
    return render(request,'main/')