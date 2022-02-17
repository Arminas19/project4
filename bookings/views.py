from django.shortcuts import render, HttpResponse
from django.views import generic

def index(request):
    return render(request, 'index.html', context=None)

