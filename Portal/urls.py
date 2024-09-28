from django.contrib import admin
from django.urls import path, include
from contractors import views  # Import views from the contractors app
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Home page showing contractor list
    path('about/', views.about, name='about'),
    path('contractors/', include('contractors.urls')),  # Include the contractors app's URLs
    path('users/', include('users.urls')),  # Include the contractors app's URLs
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('incident/', include('incident.urls')),
    
]
