from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    # pk의 역순으로 쓰는 order_by('-pk') 그냥 pk 만 쓰면 반대로 
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)

@login_required
def create(request):
    if request.method == 'POST' :
        # POST /articles/new/ => (구) craete 함수
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:index')
    
    else :
        # GET /articles/new/
        form = ArticleForm
    #공용 context
    context = {
        'form' : form
    }
    return render(request, 'articles/form.html', context)

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)

@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    article.delete()
    return redirect(f'/articles/')

def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        # instance = article 을 써주면 새 글생성이 아니라 기존 글을 가져와서 수정!
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else :
        # 수정시 해당 article의 instance를 반드시 넘겨줘야 한다.
        form = ArticleForm(instance=article)
    context = {
        'form' : form
    }
    return render(request, 'articles/form.html', context)
    
