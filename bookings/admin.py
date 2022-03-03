from django.contrib import admin
from .models import bookTable
from django_summernote.admin import SummernoteModelAdmin



admin.site.register(bookTable)
