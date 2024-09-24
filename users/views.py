from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import UserForm




def user_create_edit(request, user_id=None):
    user = None
    if user_id:
        user = get_object_or_404(User, id=user_id)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
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
        'user_obj': user  # For checking if we are editing
    })

def user_archive(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.is_active = False  # Soft delete by deactivating user
    user.save()
    messages.success(request, 'User archived successfully!')
    return redirect('user_create')
