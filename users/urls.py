from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.user_create_edit, name='user_create'),  # This handles both create and list
    path('edit/<int:user_id>/', views.user_create_edit, name='user_edit'),
    path('<int:user_id>/send_reset_email/', views.send_reset_email, name='send_reset_email'),
    path('archive/<int:user_id>/', views.user_archive, name='user_archive'),
    #path('list/', views.user_list, name='user_list'),
]
