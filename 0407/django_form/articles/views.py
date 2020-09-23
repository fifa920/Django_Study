from django.shortcuts import render, redirect, get_object_or_404
from .models import Article

# Create your views here.
def index(request):
    # pk의 역순으로 쓰는 order_by('-pk') 그냥 pk 만 쓰면 반대로 
    articles = Article.objects.order_by('-pk')
    context = {
        'articles' : articles
    }
    return render(request, 'articles/index.html', context)