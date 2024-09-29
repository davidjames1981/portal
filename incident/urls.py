from django.urls import path
from . import views

app_name = 'incident'

urlpatterns = [
    path('', views.incident_home, name='incident_home'),  
    path('submit/', views.submit_incident, name='submit_incident'),
    path('company/', views.company_incidents, name='company_incidents'),

]