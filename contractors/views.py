from django.shortcuts import render, redirect, get_object_or_404
from .models import Contractor
from .forms import ContractorForm

def contractor_list(request):
    contractors = Contractor.objects.filter(is_archived=False)
    return render(request, 'contractors/contractor_list.html', {'contractors': contractors})

def contractor_create(request):
    if request.method == 'POST':
        form = ContractorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contractor_list')
    else:
        form = ContractorForm()
    return render(request, 'contractors/contractor_form.html', {'form': form})

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
    return redirect('contractor_list')
