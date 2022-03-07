from django.shortcuts import render, HttpResponse, get_object_or_404
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.views import generic, View
from .models import newbookTable, newBooking, TableInverntory
from .forms import BookTableForm, BookPeople

def index(request):
    return render(request, 'index.html', context=None)

def login(request):
    return render(request, 'login.html', context=None)

def signUp(request):
    return render(request, 'Sign-up.html', context=None)
    
def loggedin(request):
    return render(request, 'logged-in.html', context=None)


class BookingTables(TemplateView):
    template_name = 'book-tables.html'

    def get(self, request):
        form = BookTableForm()
        form2 = BookPeople()
        return render(request, 'book-table.html', context={'form': form, 'form2': form2})

    def post(self, request, *args, **kwargs):
        form = BookTableForm(data=request.POST)
        form2 = BookPeople(data=request.POST)
        Table_booked = False
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            people = request.POST['people']
            pick_date = request.POST['pick_date']
            pick_time = request.POST['pick_time']
            
            if len(people) <= 5 and len(people) > 0:
                Tables == +1
                if len(people) > 5 and len(people) <= 10:
                    Tables == +2
                    if len(people) >= 10 and len(people) <=15:
                        Tables == +3
                        if len(people) >=15 and len(people) <=20:
                            Tables == +4
                            
            if Tablecount > Tables:
                Tables_available = True
            else:
                Tables_available = False
                return f'There isnt anymore tables left.'

            if first_name and last_name in request.POST['pick_date'].exists():
                return print('cannot book you here again, please pick a different date.')



            
            Table_booked = True

            BookTable = bookTable(people=people)
            BookTable.save()

            Booking = Booking(first_name=first_name, last_name=last_name, pick_date=pick_date, pick_time=pick_time)
            Booking.save()

        else:
            form = BookTableForm()
            from2 = BookPeople()


        return render(request, 'book-table.html', context={'form': form, 'form2': form2, 'Table_booked': Table_booked})
