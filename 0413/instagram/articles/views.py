from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from . models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

def create(request):
    if request.method == "POST":
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            # form.save()
            return redirect('articles:detail', article.pk)
        messages.error(request, 'form 다시 확인 ㄱㄱ')
    else :
        form = ArticleForm()
    context = {
        'form' : form
    }
    return render(request, 'articles/forms.html', context)

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)