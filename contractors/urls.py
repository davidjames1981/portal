from django.urls import path
from . import views

urlpatterns = [
    path('', views.contractor_create_edit, name='contractor_create'),
    path('edit/<int:contractor_id>/', views.contractor_create_edit, name='contractor_edit'),
    path('archive/<int:pk>/', views.contractor_archive, name='contractor_archive'),
   

]