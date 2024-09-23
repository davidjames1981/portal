from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('<int:user_id>/', views.manage_users, name='edit_user'),  # Edit specific user
    path('team/delete/<int:user_id>/', views.delete_user, name='delete_user'),  # Add this
    path('team/', views.manage_users, name='manage_users'),
]

