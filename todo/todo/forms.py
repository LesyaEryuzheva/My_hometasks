from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea, DateTimeInput, CharField, PasswordInput, Form, ValidationError
from .models import Todo


class TodoForm(ModelForm):

    class Meta:
        model = Todo
        fields = ['date', 'description']

        widgets = {
            'date': DateTimeInput(attrs={
                'class': 'form-control',
                'type': 'datetime-local'
            }),
            'description': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
        }


class UserRegistrationForm(ModelForm):
    password = CharField(label='Password', widget=PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')


class LoginForm(Form):
    username = CharField()
    password = CharField(widget=PasswordInput)
