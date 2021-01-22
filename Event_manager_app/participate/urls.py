from django.contrib import admin
from django.urls import path,include
from participate import views

urlpatterns = [
    path('', views.form, name = "Participate Registration Form"),
]