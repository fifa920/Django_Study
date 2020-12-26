from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import *

# Create your views here.

def index(request):
    todos = Todo.objects.all()
    content = {
        'todos' : todos
    }
    return render(request, 'todoapp/index.html', content)

def createTodo(request):
    user_input_str = request.POST['todoContent']
    new_todo = Todo(content = user_input_str)
    new_todo.save()
    return redirect('index')
    # return HttpResponse("create Todo => "+ user_input_str)

def doneTodo(request):
    done_todo_id = request.GET['todoNum']
    print("완료한 todo의 id : ", done_todo_id)
    todo = Todo.objects.get(id = done_todo_id)
    todo.isDone = True
    todo.save()
    return redirect('index')