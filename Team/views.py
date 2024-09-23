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
        user_form = UserForm(instance=user)
        profile_form = ProfileForm(instance=user.profile)
    else:
        user_form = UserForm()
        profile_form = ProfileForm()

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user if user_id else None)
        profile_form = ProfileForm(request.POST, instance=user.profile if user_id else None)

        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        if password and password == password_confirm:
            if user_form.is_valid() and profile_form.is_valid():
                try:
                    user = user_form.save(commit=False)
                    user.set_password(password)  # Set the password securely
                    user.save()

                    # Check if profile exists, update it if so, or create a new one.
                    if not user.profile:
                        profile = profile_form.save(commit=False)
                        profile.user = user
                        profile.save()

                    return redirect('manage_users')
                except IntegrityError:
                    user_form.add_error(None, "A profile for this user already exists.")
        else:
            user_form.add_error('password', 'Passwords do not match')

    users = User.objects.all()
    return render(request, 'team/manage_users.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'users': users
    })
