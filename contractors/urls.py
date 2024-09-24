from django.urls import path
from . import views

urlpatterns = [
    path('', views.contractor_list, name='contractor_list'),
    path('create/', views.contractor_create, name='contractor_create'),
    path('edit/<int:pk>/', views.contractor_edit, name='contractor_edit'),
    path('archive/<int:pk>/', views.contractor_archive, name='contractor_archive'),
]
