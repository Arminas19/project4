from django.views import generic, View
from . import views
from django.urls import path


urlpatterns = {
   path('', views.index, name='home'),
}