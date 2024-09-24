from django.shortcuts import render, redirect, get_object_or_404
from .models import Contractor
from .forms import ContractorForm

def contractor_list(request):
    contractors = Contractor.objects.filter(is_archived=False)
    return render(request, 'contractors/contractor_list.html', {'contractors': contractors})


from django.shortcuts import render, redirect
from .forms import ContractorForm

from django.contrib import messages

def contractor_create_edit(request, contractor_id=None):
    contractor = None
    if contractor_id:
        contractor = get_object_or_404(Contractor, id=contractor_id)

    if request.method == 'POST':
        form = ContractorForm(request.POST, instance=contractor)
        if form.is_valid():
            form.save()
            if contractor_id:
                messages.success(request, 'Contractor updated successfully!')
            else:
                messages.success(request, 'Contractor added successfully!')
            return redirect('contractor_create')  # Redirect to contractor list after save
    else:
        form = ContractorForm(instance=contractor)

    contractors = Contractor.objects.filter(is_archived=False)  # Only non-archived contractors
    return render(request, 'contractors/contractor_form.html', {
        'form': form,
        'contractors': contractors,
        'contractor': contractor  # For checking if we're editing
    })



def contractor_create(request):
    if request.method == 'POST':
        form = ContractorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contractor_create')
    else:
        form = ContractorForm()

    # Filter contractors that are not archived
    contractors = Contractor.objects.filter(is_archived=False)
    return render(request, 'contractors/contractor_form.html', {'form': form, 'contractors': contractors})


def contractor_edit(request, pk):
    contractor = get_object_or_404(Contractor, pk=pk)
    if request.method == 'POST':
        form = ContractorForm(request.POST, instance=contractor)
        if form.is_valid():
            form.save()
            return redirect('contractor_list')
    else:
        form = ContractorForm(instance=contractor)
    return render(request, 'contractors/contractor_form.html', {'form': form})

def contractor_archive(request, pk):
    contractor = get_object_or_404(Contractor, pk=pk)
    contractor.is_archived = True
    contractor.save()
    return redirect('contractor_create')

