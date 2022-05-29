from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from .models import Todo
from .forms import TodoForm, UserRegistrationForm, LoginForm


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
            return redirect('about')

    form = TodoForm()

    context = {
        'form': form
    }
    return render(request, 'todo/create.html', context)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=True)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'todo/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'todo/register.html', {'user_form': user_form})


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(username=data['username'], password=data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('todo')
                else:
                    return HttpResponse('Disabled todo')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'todo/login.html', {'form': form})
