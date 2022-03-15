from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator, MinValueValidator

STATUS = ((0, "Occupied"), (1, "Ordered"))

class newBooking(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    pick_date = models.DateField()
    pick_time = models.TimeField()

    def __str__(self): 
        return f' {self.first_name} {self.last_name} booked a table on the {self.pick_date} {self.pick_time} '

class newbookTable(models.Model):
    Booking = models.ForeignKey(newBooking, on_delete=models.CASCADE, related_name="tables")
    people = models.IntegerField(validators=[
            MaxValueValidator(20),
            MinValueValidator(1)
        ])

    def __str__(self):
        return f'{self.Booking} {self.people} guests will be attending. '


class TableInverntory(models.Model):
    Tablecount = models.IntegerField(default=20)
    Tables_available = models.BooleanField(default=False)

    Tables = 0