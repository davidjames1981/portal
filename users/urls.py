from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.users, name='users'),  # Home page showing contractor list
]
