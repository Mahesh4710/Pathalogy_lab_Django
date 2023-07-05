
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='index'),
    path("about", views.about, name='about'),
    path("services1", views.services1, name='services1'),
    path("signup", views.signup, name='signup'),

    path("contact", views.contact, name='contact'),


    path("appointment", views.appointment, name='appointmentd'),

]
