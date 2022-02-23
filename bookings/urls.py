from django.views import generic, View
from . import views
from django.urls import path


urlpatterns = {
   path('', views.index, name='home'),
   path('login.html', views.login, name='login'),
   path('Sign-up.html', views.signUp, name='Sign-up'),
}