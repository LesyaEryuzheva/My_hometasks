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
        else:
            print(form.errors)

    form = TodoForm()

    data = {
        'form': form
    }
    return render(request, 'todo/create.html', data)


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=True)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            print('1234')
            return render(request, 'todo/register_done.html', {'new_user': new_user})
    else:
        print('22222')
        user_form = UserRegistrationForm()
    return render(request, 'todo/register.html', {'user_form': user_form})


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(username=cd['username'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponse('Authenticated successfully')
                else:
                    return HttpResponse('Disabled todo')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'todo/login.html', {'form': form})