from django.shortcuts import render, HttpResponse
from django.views.generic.edit import CreateView
from django.views import generic
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

def bookTables(request):
    form = BookTableForm()
    mydict = {'form': form}
    return render(request, 'book-table.html', context=mydict)

