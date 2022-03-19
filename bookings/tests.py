import unittest
from django.test import TestCase
#from .views import deleteBooking, BookingTables
# to run test type: python3 bookings/test.py
# watch python Testing 'Real World Test's' to learn how to test my python code.

# Create your tests here.

class TestBookingTables(unittest.TestCase):

    def test_if_BookingTables_is_returning_allBookings(self):
        pass

    def test_if_deleteBooking_is_getting_bookings_id(self):
        pass

    def test_if_BookingTables_throws_an_errorMessage_when_an_error_occures(self):
        pass

    def test_if_BookingTables_is_setting_Table_booked_to_True(self):
        pass

unittest.main()