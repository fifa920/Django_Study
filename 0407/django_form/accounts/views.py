from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST

from .forms import CustomUserChangeForm

# Create your views here.
def signup(request):
    # 로그인이 되어 있다면
    if request.user.is_authenticated :
        # 돌아가라....(redirect)
        return redirect('articles:index')

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/signup.html', context)

# 개인 프로필 페이지 느낌
def detail(request, pk):
    User = get_user_model()
    user = get_object_or_404(User, pk=pk)
    context = {
        'user':user
    }
    return render(request, 'accounts/detail.html', context)

def update(request, pk):
    form =CustomUserChangeForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

def login(request):
    if request.user.is_authenticated :
        return redirect('articles:index')
    if request.method == 'POST' :
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 장고 내부 auth.form 에 있는 login 함수를 꺼내쓴다.
            # form.get_user() 은 Authentication 내에 있는 메소드
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else :         
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

@login_required
def logout(request):
    # 로그인이 되어 있으면 로그아웃하고
    auth_logout(request)
    return redirect('articles:index')

@require_POST
@login_required
def delete(request):
    request.user.delete()
    return redirect('articles:index')