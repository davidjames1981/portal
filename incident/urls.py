from django.urls import path
from . import views

app_name = 'incident'

urlpatterns = [
    path('', views.incident_home, name='incident_home'),  

]