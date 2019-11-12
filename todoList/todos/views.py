from django.shortcuts import render, redirect
from django.http import HttpResponse

from . models import Todo
# Create your views here.

def index(request):

    todos = Todo.objects.all()[:10]

    context = {
        'todos': todos
    }

    return render(request, 'todo/index.html', context)


def detail_page(request, id):
    todo = Todo.objects.get(id = id)

    context = {
        'todo': todo
    }

    return render(request, 'todo/details.html', context)


def add(request):
    if(request.method == 'POST'):
        title = request.POST['title']
        text = request.POST['text']

        todo = Todo(title= title, text = text)
        todo.save()

        return redirect('/todos')
    else:
        return render(request, 'todo/add.html')
