from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    return render(request, template)

def group_posts(request, slug):
    return HttpResponse(f'Пост от товарища {slug}') 
