from django.contrib import admin
from django.urls import path,include
from event import views

urlpatterns = [
    path('', views.form, name = "Event Registration Form"),
]