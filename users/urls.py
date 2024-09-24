from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.user_create_edit, name='users_form'),  # Home page showing contractor list
    path('edit/<int:user_id>/', views.user_create_edit, name='user_edit'),
    path('archive/<int:pk>/', views.user_archive, name='user_archive'),
]
