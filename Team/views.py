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

        # Check if the forms are valid
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save(commit=False)

            # Handle password update only if passwords match and are provided
            if password and password == password_confirm:
                user.set_password(password)
            elif not password and user_id:
                user.password = user.password  # Keep existing password if no new password is provided

            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            return redirect('manage_users')
        else:
            # Debugging: print form validation errors to the console
            print(user_form.errors)
            print(profile_form.errors)

    users = User.objects.all()
    return render(request, 'team/manage_users.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'users': users
    })
