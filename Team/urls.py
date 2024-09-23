from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('', views.manage_users, name='manage_users'),
    path('<int:user_id>/', views.manage_users, name='edit_user'),  # Edit specific user
]

