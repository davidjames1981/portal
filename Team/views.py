from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import UserForm

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')





def manage_users(request, user_id=None):
    if user_id:
        user = User.objects.get(pk=user_id)
        form = UserForm(instance=user)
    else:
        form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user if user_id else None)
        if form.is_valid():
            form.save()
            return redirect('manage_users')

    users = User.objects.all()
    return render(request, 'team/manage_users.html', {'form': form, 'users': users})


