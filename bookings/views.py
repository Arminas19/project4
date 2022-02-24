from django.shortcuts import render, HttpResponse
from django.views import generic

def index(request):
    return render(request, 'index.html', context=None)

def login(request):
    return render(request, 'login.html', context=None)

def signUp(request):
    return render(request, 'Sign-up.html', context=None)

def loggedin(request):
    return render(request, 'logged-in.html', context=None)

def bookTable(request):
    return render(request, 'book-table.html', context=None)