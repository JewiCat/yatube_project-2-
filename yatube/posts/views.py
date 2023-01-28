from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def index(request):
    template = 'posts/index.html'
    text = 'Это главная страница проекта Yatube'
    context = {
        'text': text
    }
    return render(request, template, context)


def group_posts(request):
    template = 'posts/group_list.html'
    text = 'Здесь будет информация о группах проекта Yatube'
    context = {
        'text2': text
    }
    return render(request, template, context)
