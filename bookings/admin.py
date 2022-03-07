from django.contrib import admin
from .models import newbookTable
from .models import newBooking
from django_summernote.admin import SummernoteModelAdmin


admin.site.register(newbookTable)
admin.site.register(newBooking)
