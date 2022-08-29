from django.shortcuts import render
from .models import Todo


def index (request):
    todos = Todo.objects.filter(title__contains=request.GET.get('search', ''))
    context = {
        'todos': todos,
    }
    return render(request,'todo/index.html', context)


def view (request, id):
    todo = Todo.objects.get(id=id)
    context = {
        'todo': todo,
    }
    return render(request,'todo/detail.html', context)

def edit (request, id):
    return render(request,'todo/index.html', {})

def add (request):
    return render(request,'todo/index.html', {})

def delete (request, id):
    return render(request,'todo/index.html', {})


