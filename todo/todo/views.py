from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoForms


def index(request):
    return render(request, 'todo/index.html')


def about(request):
    todos = Todo.objects.order_by('date').all()
    data = {
        'todos': todos
    }
    return render(request, 'todo/about.html', data)


def create(request):
    error = ''
    if request.method == 'POST':
        form = TodoForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
        else:
            error = 'Ошибка'

    form = TodoForms()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'todo/create.html', data)
