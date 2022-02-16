from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Occupied"), (1, "Ordered"))

class BookTable(models.Model):
    people = models.IntegerField()
    pick_date = models.DateField()