from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForm


def index(request):
    return render(request, 'todo/index.html')


def about(request):
    todos = Todo.objects.order_by('date').all()
    data = {
        'todos': todos
    }
    return render(request, 'todo/about.html', data)


def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
        else:
            print(form.errors)

    form = TodoForm()

    data = {
        'form': form
    }
    return render(request, 'todo/create.html', data)
