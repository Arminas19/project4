from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.views import generic, View
from .models import bookTable
from .forms import BookTableForm

def index(request):
    return render(request, 'index.html', context=None)

def login(request):
    return render(request, 'login.html', context=None)

def signUp(request):
    return render(request, 'Sign-up.html', context=None)
    
def loggedin(request):
    return render(request, 'logged-in.html', context=None)

# def bookTables(request):
#     form = BookTableForm()
#     mydict = {'form': form}
#     return render(request, 'book-table.html', context=mydict)

class BookingTables(TemplateView):
    template_name = 'book-tables.html'

    def get(self, request):
        form = BookTableForm()
        return render(request, 'book-table.html', context={'form': form})

    def post(self, request, *args, **kwargs):
        form = BookTableForm(data=request.POST)
        if form.is_valid():
            form = BookTableForm()
            
        else:
            form = BookTableForm()

        return render(request, 'book-table.html', context={'form': form })