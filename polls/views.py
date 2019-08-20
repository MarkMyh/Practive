from django.shortcuts import render
from django.http import HttpResponse
from . import models


# Create your views here.

def index(request):
    articles = models.Article.objects.all()
    # return HttpResponse("hello")
    return render(request, 'index.html', {'articles': articles})


def article_page(request, article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request, 'Article_page.html', {'article': article})


def edit_page(request):
    # article = models.Article.objects.get(pk=article_id)
    return render(request, 'Edit_page.html')


def edit_action(request):
    title = request.POST.get('title', 'TITLE')
    content = request.POST.get('content', 'CONTENT')
    models.Article.objects.create(title=title, content=content)
    articles = models.Article.objects.all()
    # return HttpResponse("hello")
    return render(request, 'index.html', {'articles': articles})
