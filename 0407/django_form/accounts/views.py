from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout

from .forms import CustomUserChangeForm

# Create your views here.
def signup(request):
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
    if request.method == 'POST' :
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 장고 내부 auth.form 에 있는 login 함수를 꺼내쓴다.
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else :         
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')