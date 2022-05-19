from .models import Todo
from django.forms import ModelForm, TextInput, DateTimeInput


class TodoForms(ModelForm):
    class Meta:
        model = Todo
        fields = ['date', 'description']

        widgets = {
            "date": DateTimeInput(attrs={
                'class': "form-control",
                'type': "datetime-local"
            }),
            "description": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Описание'
            }),
        }
