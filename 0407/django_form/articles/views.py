from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article':article
    }
    return render(request, 'articles/detail.html', context)
