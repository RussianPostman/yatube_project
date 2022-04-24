from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

def index(request):
    posts = Post.objects.order_by('-pub_date')[:10]
    context = {
        'posts': posts,
    }
    return render(request, 'posts/index.html', context) 

def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    mesege = f'Пост от товарища {slug}'
    context = {
        'title': title,
        'mesege': mesege,
    }
    return render(request, template, context)