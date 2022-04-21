from django.views import generic, View
from . import views
from django.urls import path


urlpatterns = [
   path('', views.index, name='home'),
   path('login.html', views.login, name='login'),
   path('Sign-up.html', views.signUp, name='Sign-up'),
   path('logged-in.html', views.loggedin, name='logged-in'),
   path('book-table.html', views.BookingTables.as_view(), name='book-table'),
   path('edit-booking/<booking_id>', views.edit_bookings, name='edit_booking'),
   path('delete/<booking_id>/<booking_id>', views.deleteBooking, name='delete_booking'),
   path('view-bookings.html', views.view_bookings, name='view_bookings'),
]