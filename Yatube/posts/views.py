from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    template = 'posts/index.html'
    title = "Это главная страница проекта Yatube"
    context = {
        'title': title,
    }
    return render(request, template, context)

def group_posts(request, slug):
    template = 'posts/group_list.html'
    title = 'Здесь будет информация о группах проекта Yatube'
    mesege = f'Пост от товарища {slug}'
    context = {
        'title': title,
        'mesege': mesege,
    }
    return render(request, template, context)
   