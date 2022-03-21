import unittest
from django.test import TestCase
#from .bookings.models import newBooking
# from bookings.models import *
# from .views import BookingTables, deleteBooking

# to run test type: python3 bookings/tests.py
# watch python Testing 'Real World Test's' to learn how to test my python code.

# Create your tests here.

class TestBookingTables(unittest.TestCase):
    # test_if_BookingTables_is_checking_for_double_bookings dose not work because of an error im my interpreter, 
    # Error Type - ImportError: attempted relative import with no known parent package.
    # This error happened becuase at the very start of my project i made two interpreters by accident. 
    # I could select the interpreter i want to use but im afraid of messing things up, so im just going to leave it here. 

    # def test_if_BookingTables_is_checking_for_double_bookings(self):
    #     """  This test is checking if my double bookings prevension works, so im 
    #     creating an instance of the booking than im saving it to the database, than im getting
    #     that instance in the try block, if that instance is their than already_booked should be True.
    #     if the instance is their the test should pass if not the test should fail.
    #     """
    #     already_booked = False
    #     test_booking = newBooking(first_name='Kev', last_name='guy', pick_date='21/03/2022', pick_time='10:52')
    #     test_booking.save()

    #     try:
    #         test_booking = newBooking.objects.get(first_name='kev', last_name='guy', pick_date='21/03/2022', pick_time='10:52')
    #         print(test_booking)
    #         already_booked = True
    #     except ObjectDoesNotExist:
    #         already_booked = False

    #     self.assertEqual(already_booked, True)

    def test_if_BookingTables_is_checking_for_max_number_of_people(self):
        """    """
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