from django.forms import ModelForm, Textarea, DateTimeInput
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
