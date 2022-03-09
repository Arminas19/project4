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
            errorMessage = None
            
            # if len(people) <= 5 and len(people) > 0:
            #     TableInverntory.Tables == +1
            #     if len(people) > 5 and len(people) <= 10:
            #         TableInverntory.Tables == +2
            #         if len(people) >= 10 and len(people) <=15:
            #             TableInverntory.Tables == +3
            #             if len(people) >=15 and len(people) <=20:
            #                 TableInverntory.Tables == +4
                            
            # if TableInverntory.Tablecount > TableInverntory.Tables:
            #     TableInverntory.Tables_available = True
            # else:
            #     TableInverntory.Tables_available = False
            #     errorMessage = 'There isnt enough tables, please book a different time!.'

            newBooking_first_name =  newBooking.objects.filter(first_name__exact=first_name)
            newBooking_last_name =  newBooking.objects.filter(last_name__exact=last_name)
            newBooking_pick_date =  newBooking.objects.filter(pick_date__exact=pick_date)

            if newBooking_first_name == first_name  and newBooking_last_name == last_name and newBooking_pick_date == pick_date:
                # If user is found display an error message.
                errorMessage = 'This User has already booked a table with us.'
           
            

            if not errorMessage:
                Booking = newBooking(first_name=first_name, last_name=last_name, pick_date=pick_date, pick_time=pick_time)
                Booking.save()

                BookTabless = newbookTable(people=people, Booking=Booking)
                BookTabless.save()

                Table_booked = True
        else:
            form = BookTableForm()
            from2 = BookPeople()
            return render(request, 'book-table.html', context={'errorMessage': errorMessage})


        return render(request, 'book-table.html', context={'form': form, 'form2': form2, 'Table_booked': Table_booked})
