from tkinter import Widget
from django.forms import ModelForm, DateInput
from .models import Todo

class TodoForm(ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'
        Widgets = {'updated_at': DateInput(attrs={'class': 'form-control'}),}