from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Occupied"), (1, "Ordered"))

class bookTable(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    people = models.IntegerField()
    pick_date = models.DateField()
    pick_time = models.DateTimeField()
   