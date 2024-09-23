from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm
from django.db import IntegrityError


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return redirect('manage_users')

def manage_users(request, user_id=None):
    if user_id:
        user = User.objects.get(pk=user_id)
        user_form = UserForm(request.POST or None, instance=user)
        profile_form = ProfileForm(request.POST or None, instance=user.profile)
    else:
        user_form = UserForm(request.POST or None)
        profile_form = ProfileForm(request.POST or None)

    if request.method == 'POST':
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)

            # Update password only if provided
            if password and password == password_confirm:
                user.set_password(password)
            elif not password and user_id:
                user.password = user.password  # Don't change the password if no new one is provided

            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('manage_users')
        else:
            if password != password_confirm:
                user_form.add_error('password', 'Passwords do not match')

    users = User.objects.all()
    return render(request, 'team/manage_users.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'users': users
    })

