from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Occupied"), (1, "Ordered"))

class bookTable(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    people = models.IntegerField()
    pick_date = models.DateField()
    pick_time = models.TimeField()

    def __str__(self):
        return f' {self.first_name} {self.last_name} booked a table on the {self.pick_date} {self.pick_time} with {self.people} people'
   