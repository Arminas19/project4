from django.shortcuts import render, HttpResponse
from django.views import generic
from django.views.generic import CreateView
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
    model = bookTable
    context = {'form': form}
    return render(request, 'book-table.html', context)

