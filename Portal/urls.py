from django.contrib import admin
from django.urls import path, include
from contractors import views  # Import views from the contractors app
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page showing contractor list
    path('about/', views.about, name='about'),
    path('contractors/', include('contractors.urls')),  # Include the contractors app's URLs
]
