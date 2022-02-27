from django import forms
from django.forms import ModelForm
from .models import bookTable


class BookTableForm(ModelForm):
    class Meta:
        model = bookTable 
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'people': forms.NumberInput(attrs={'class': 'form-control'}),
            'pick_date': forms.DateInput(attrs={'class': 'form-control'}),
            'pick_time': forms.TimeInput(attrs={'class': 'form-control'}),
        }