from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic.edit import CreateView
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

def bookTables(request):
    form = BookTableForm()
    mydict = {'form': form}
    return render(request, 'book-table.html', context=mydict)

class BookingTables(View):

    def get(self, request, *args, **kwargs):

        BookTableForm = BookTableForm()
        if BookTableForm.is_vaild():
            BookTableForm.instance.first_name = request.user.first_name
            BookTableForm.instance.last_name = request.user.last_name
            BookTableForm.instance.people = request.user.people
            BookTableForm.instance.pick_date = request.user.pick_date
            BookTableForm.instance.pick_time = request.user.pick_time
            bookTable.save()
        else:
            BookTableForm = BookTableForm()


        return render(request, 'book-table.html', context={
            'form': form
        },)

    def post(self, request, *args, **kwargs):

        BookTableForm = BookTableForm()
        if BookTableForm.is_vaild():
            BookTableForm.instance.first_name = request.user.first_name
            BookTableForm.instance.last_name = request.user.last_name
            BookTableForm.instance.people = request.user.people
            BookTableForm.instance.pick_date = request.user.pick_date
            BookTableForm.instance.pick_time = request.user.pick_time
            bookTable.save()
        else:
            BookTableForm = BookTableForm()


        return render(request, 'book-table.html', context={
            'form': form
        },)