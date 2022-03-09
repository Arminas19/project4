from django import forms
from django.forms import ModelForm
from .models import newbookTable
from .models import newBooking


class DateInput(forms.DateInput):
    input_type = 'pick_date'


class BookTableForm(ModelForm):
    class Meta:
        model = newBooking 
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Brian'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Smite'}),
           'pick_date': forms.DateInput(
                format=('%d/%m/%Y'),
                attrs={'class': 'form-control', 
                       'placeholder': 'Select a date',
                       'type': 'date' 
                      }),
            'pick_time': forms.TimeInput(
                format=('%H:%M'),
                attrs={'class': 'form-control',
                'placeholder': 'Select a Time',
                'type' : 'time'
                }),
        }

    def clean_name(self):
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        for instance in newBooking.objects.all():
            if instance.first_name == first_name and instance.last_name == last_name:
                raise forms.ValidationError('That name is already Booked!')
            return first_name and last_name


class BookPeople(ModelForm):
    class Meta:
        model = newbookTable
        fields = ('people',)
        widgets = {
            'people': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '3'}),
        }

