from django.shortcuts import render
from .models import Todo

# Create your views here


def index(request):
    return render(request, 'todo/index.html')

def about(request):
    todos = Todo.objects.all()
    data = {
        'todos' : todos
    }
    return render(request, 'todo/about.html', data)