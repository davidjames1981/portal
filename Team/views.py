from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm
from django.db import IntegrityError





def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
