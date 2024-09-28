from django.contrib import admin
from django.urls import path, include
from . import views

app_name ='users'

urlpatterns = [

    path('', views.user_create_edit, name='user_create'),  # This handles both create and list
    path('edit/<int:user_id>/', views.user_create_edit, name='user_edit'),
    path('user_create/<int:user_id>/', views.user_create_edit, name='user_create'),
    path('archive/<int:user_id>/', views.user_archive, name='user_archive'),
]
