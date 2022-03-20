import unittest
# from .models import newBooking, newbookTable, TableInverntory
# from .views import BookingTables, deleteBooking
from django.test import TestCase

# to run test type: python3 bookings/tests.py
# watch python Testing 'Real World Test's' to learn how to test my python code.

# Create your tests here.

class TestBookingTables(unittest.TestCase):

    def test_if_BookingTables_is_checking_for_double_bookings(self):
        pass

    def test_if_BookingTables_is_checking_for_max_number_of_people(self):
        pass

    def test_if_BookingTables_throws_an_errorMessage_when_an_error_occures(self):
        """ Here im checking if the errorMessage logic is doing what i intend it to do.
            Im trying to see if the errorMessage activates and prevents 'a' from changing to a 6,
            If the a changes to a 6 that means that the errorMessage didn't work. 
        """
        errorMessage = None
        a = 7
        try:
            if a == 7:
                errorMessage = 'This is the errorMessage'
            else:
                errorMessage = False
        except Exception as errorMessage:
            print('errorMessage didnt come true')
            errorMessage = False
        if not errorMessage:
            a == 6
            print('errorMessage didnt come true')
            errorMessage = False
        else:
            print('success')
        if a == 6:
            print('fail')
        else:
            print('success')
            errorMessage = True
            
        self.assertEqual(errorMessage, True)

    def test_if_BookingTables_is_setting_Table_booked_to_True(self):
        """ Here im am checking if Table_booked is getting set to True once the validation's are complete
        and no error's occure, im testing this because i will be using this method to throw a success's message once the user
        book's a table with the resturaunt. 
        """
        Table_booked = False
        error = True
        conditions_met = False
        form_is_valid = True
        
        if form_is_valid == True:
            conditions_met = True
            print('conditions_met is True')
        else:
            conditions_met = False

        No_errors = True

        if No_errors == True:
            error = False
            print('No error has occuered')

        else:
            error = True

        if error == False and conditions_met == True:
            print('Table_booked is True')
            Table_booked = True

        self.assertEqual(error, False)
        self.assertEqual(conditions_met, True)
        self.assertEqual(Table_booked, True)
        

unittest.main()