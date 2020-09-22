from django.shortcuts import render, redirect
from .models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)
    
def new(request):
    return render(request, 'articles/new.html')

def create(request):
    article = Article()
    article.title = request.POST.get('title')
    article.content = request.POST.get('content')
    article.save()
    return redirect(f'/articles/')

def detail(request, pk):
    article = Article.objects.get(id=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect(f'/articles/')

def edit(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/edit.html', context)

def update(reqeust, pk):
    article = Article.objects.get(pk=pk)
    article.title = reqeust.POST.get('title')
    article.content = reqeust.POST.get('content')
    article.save()
    return redirect(f'/articles/{article.pk}/')