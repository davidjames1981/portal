from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


@login_required
def user_create_edit(request, user_id=None):
    user = None
    if user_id:
        user = get_object_or_404(User, id=user_id)
        profile = Profile.objects.get(user=user)  # Load the user's profile
    else:
        profile = None

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save(commit=False)

            # Set password if provided
            password = form.cleaned_data.get('password')
            if password:
                user.set_password(password)

            user.save()

            # Save or update the profile data
            profile, created = Profile.objects.get_or_create(user=user)
            profile.mobile_phone = form.cleaned_data.get('mobile_phone')
            profile.company = form.cleaned_data.get('company')
            profile.save()

            messages.success(request, 'User saved successfully!')
            return redirect('user_create')
    else:
        # Populate form with user and profile data
        form = UserForm(instance=user, initial={
            'mobile_phone': profile.mobile_phone if profile else '',
            'company': profile.company if profile else None
        })

    users = User.objects.filter(is_active=True)
    return render(request, 'users/user_form.html', {
        'form': form,
        'users': users,
        'user_obj': user
    })



@login_required
def user_archive(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = False  # Soft delete by deactivating user
    user.save()
    messages.success(request, 'User archived successfully!')
    return redirect('user_create')
