from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.core.exceptions import ObjectDoesNotExist
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
        # form2 display's the newbookTable model onto the view.
        # form is newBooking model.
        form = BookTableForm(data=request.POST)
        form2 = BookPeople(data=request.POST)
        # Table_booked is used to show a success message after the booking is complete. 
        Table_booked = False
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            people = request.POST['people']
            pick_date = request.POST['pick_date']
            pick_time = request.POST['pick_time']
            errorMessage = None
            Bookings = newBooking.objects.all()
            

            # This code here is getting the first, last name and the date that the user has selected and checking if it exist's, 
            # if it dose exist than dislpay the errorMessage, if not than proceed with the next validation.
            try:
                already_booked = newBooking.objects.filter(first_name=first_name, last_name=last_name, pick_date=pick_date).get()
                print(already_booked)
                errorMessage = 'Sorry only one booking per person per same date allowed.'
            except ObjectDoesNotExist:
                already_booked = False
                try:
                    print('2nd try')
                    already_full = newBooking.objects.filter(pick_date=pick_date)
                    for booking in already_full:
                        print(booking)
                    booked_people = []
                    for bookings in already_full:
                        booked_people.append(bookings.people)
                    number_of_booked = sum(booked_people)
                    print(number_of_booked + 'this is number_of_booked')
                    if number_of_booked <= 18:
                        errorMessage = 'Sorry please book a different date, we are already full!, Thank You'
                except:
                    already_full = False
                
              
            # try:
            #     # already_full = newbookTable.objects.select_related('Booking').filter(Booking__pick_date = pick_date)
            #     # print(already_full, 'already full')
            #     # if len(already_full) >= 1:
            #     #     errorMessage = 'Sorry only one booking per person per timeslot, Thank You'
            #     #     return render(request, 'book-table.html', context={'form': form, 'form2': form2, 'Table_booked': Table_booked, 'errorMessage': errorMessage, 'Bookings': Bookings})
            #     if: 
            #         # Im getting the user's selected date here. im using the newbookTable model here becuase their is a foreignKey which i can use to 
            #         # check the user's selected date and also the people queryset in the newbookTable objects.
            #         already_full = newbookTable.objects.select_related('Booking').filter(Booking__pick_date = pick_date).get()
            #         # Im going to get the number of people in the user's selected date here. 
            #         print(already_full)
            #         people = already_full.people
            #         print(people)
            #         print('-------------------------------------------')
            #         # Here im checking if the number of people in that date is lower or equals to the max_number of people allowed. 
            #     if len(people) in already_full <= 18:
            #         # If the conditions meet, this will display the errorMessage that will prevent the user from booking. 
            #         print(len(people))
            #         errorMessage = 'Sorry please book a different date, we are already full!, Thank You'
            # except:
            #     # if no errorMessages are displayed, the booking procceds.
            #     print(len(people))
            #     already_full = False
              
        
            
            # if no errorMessage are displayed than this will save both the forms.
            if not errorMessage:
                Booking = newBooking(first_name=first_name, last_name=last_name, pick_date=pick_date, pick_time=pick_time)
                Booking.save()

                BookTabless = newbookTable(people=people, Booking=Booking)
                BookTabless.save()

                Table_booked = True
        else:
            # if the errorMessage dose display this will return empty forms back to the user. 
            form = BookTableForm()
            from2 = BookPeople()
            return render(request, 'book-table.html', context={})


        return render(request, 'book-table.html', context={'form': form, 'form2': form2, 'Table_booked': Table_booked, 'errorMessage': errorMessage, 'Bookings': Bookings})

class cancelle_reservations(TemplateView):
    template_name = 'cancellations.html'
    model = newbookTable

    def get(self, request, Booking_id):
        bookTables = newbookTable.objects.all()
        Bookings = newBooking.objects.all()
        Bookings = get_object_or_404(newBooking, id=Booking_id)
        form = BookTableForm(instance=Bookings)
        form2 = BookPeople(instance=Bookings)
        context = {
        'form': form,
        'form2': form2,
        'bookTables': bookTables,
        'Bookings': Bookings
        }
        return render(request, 'cancellations.html', context)
