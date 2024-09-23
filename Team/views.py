from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from .forms import UserForm, ProfileForm


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

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('manage_users')

    users = User.objects.all()
    return render(request, 'team/manage_users.html', {
        'user_form': user_form,
        'profile_form': profile_form,
        'users': users
    })


