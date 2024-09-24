from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserForm

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



def user_create_edit(request, user_id=None):
    user = None
    if user_id:
        user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)

            # Set password only if a new password has been provided
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)

            user.save()
            if user_id:
                messages.success(request, 'User updated successfully!')
            else:
                messages.success(request, 'User added successfully!')
            return redirect('user_create')
    else:
        form = UserForm(instance=user)

    users = User.objects.filter(is_active=True)
    return render(request, 'users/user_form.html', {
        'form': form,
        'users': users,
        'user_obj': user
    })



def user_archive(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = False  # Soft delete by deactivating user
    user.save()
    messages.success(request, 'User archived successfully!')
    return redirect('user_create')
