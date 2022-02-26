from django import forms
from django.forms import ModelForm
from .models import bookTable


class DateInput(forms.DateInput):
    input_type = 'date'


class BookTableForm(ModelForm):
    class Meta:
        model = bookTable 
        fields = ['first_name', 'last_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'people': forms.TextInput(attrs={'class': 'form-control'}),
            'pick_date': forms.TextInput(attrs={'class': 'form-control'}),
            'pick_time': forms.TextInput(attrs={'class': 'form-control'}),
        }