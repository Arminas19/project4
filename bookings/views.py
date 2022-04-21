from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView, DeleteView, ListView, CreateView
from django.core.exceptions import ObjectDoesNotExist
from django.views import generic, View
from django.urls import reverse_lazy, reverse
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


class BookingTables(CreateView):
    template_name = 'book-tables.html'
  
    def get(self, request):
        form = BookTableForm()
        form2 = BookPeople()
        return render(request, 'book-table.html', context={'form': form, 'form2': form2})

    def post(self, request, *args, **kwargs):
        model = newBooking
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
            allBookings = newBooking.objects.all()
            # newBooking.objects.create(first_name=first_name, last_name=last_name, pick_date=pick_date, pick_time=pick_time)

            # This code here is getting the first, last name and the date that the user has selected and checking if it exist's, 
            # if it dose exist than dislpay the errorMessage, if not than proceed with the next validation.
            try:
                already_full = newBooking.objects.filter(first_name=first_name, last_name=last_name, pick_date=pick_date).get()
                print(already_full)
                errorMessage = 'Sorry booking on the same date is not allowed, please pick a different date.'
            except ObjectDoesNotExist:
                already_full = False
                try:
                    print('2nd try')
                    already_full = newBooking.objects.filter(pick_date=pick_date).all()
                    number_of_booked = 0
                    for reservation in already_full:
                        tables = reservation.tables.all()
                        for table in tables:
                            number_of_booked += table.people
                    if number_of_booked >= 100:
                        errorMessage = 'Sorry please book a different date, we are already full!, Thank You'
                except Exception as err:
                    print(err)    
            
            # if no errorMessage are displayed than this will save both the forms.
            if not errorMessage:
                Booking = newBooking(first_name=first_name, last_name=last_name, pick_date=pick_date, pick_time=pick_time)
                booking_id = Booking.id
                Booking.save()
                # print(BookingID)
                BookTabless = newbookTable(people=people, Booking=Booking)
                BookTabless.save()
                
                Table_booked = True
                return render(request, 'book-table.html', context={'form': form, 'form2': form2, 'Table_booked': Table_booked, 'errorMessage': errorMessage, 'booking_id': booking_id, 'allBookings': allBookings})
        else:
            # if the errorMessage dose display this will return empty forms back to the user. 
            form = BookTableForm()
            from2 = BookPeople()
            return render(request, 'book-table.html', context={})

        return render(request, 'book-table.html', context={'form': form, 'form2': form2, 'Table_booked': Table_booked, 'errorMessage': errorMessage, 'allBookings': allBookings})

    # This function get's the id of the booking that was made by the user and deletes it.
    # it's called when the user presses the 'Cancelle Reservation' button.


def edit_bookings(request, booking_id):

    if request == 'POST':
        booking = newBooking.objects.get(id=booking_id)
        form = BookTableForm(instance=booking)
        if form.is_valid():
            form.save()
            return redirect(reverse('view-bookings.html'))
        else:
            errorMessage = 'Error in the Booking'
    else:
        booking = newBooking.objects.get(id=booking_id)
        form = BookTableForm(instance=booking)

    template = 'edit-booking.html'
    context = {
        'form': form,
        'errorMessage': errorMessage
    }

    return render(request, template, context)
    

def deleteBooking(request, booking_id):
    newBooking.objects.get(id=booking_id).delete()
    return redirect(reverse('logged-in'))


def view_bookings(request):
    errorMessage = None
    Table_booked = True
    allBookings = newBooking.objects.all()

    return render(request, 'view-bookings.html', context={'Table_booked': Table_booked, 'errorMessage': errorMessage, 'allBookings': allBookings})