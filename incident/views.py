from django.shortcuts import render, redirect, get_object_or_404
from .models import WorkIncident
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def incident_home(request):
    return render(request, 'incident/incident.html')



@login_required
def submit_incident(request):
    if request.method == 'POST':
        company = request.POST.get('company')
        incident_type = request.POST.get('incident_type')
        incident_date = request.POST.get('incident_date')
        location = request.POST.get('location')
        description = request.POST.get('description')
        severity = request.POST.get('severity')
        action_taken = request.POST.get('action_taken')

        # Create a new WorkIncident object
        WorkIncident.objects.create(
            reported_by=request.user,
            incident_date=incident_date,
            location=location,
            incident_type=incident_type,
            description=description,
            severity=severity,
            action_taken=action_taken,
            company=company,
        )

        messages.success(request, 'Incident reported successfully!')
        return redirect('incident:incident_home')

    return render(request, 'incident/submit_incident.html', {'user': request.user})



@login_required
def company_incidents(request):
    # Get all incidents related to the logged-in user's company
    company_name = request.user.profile.company
    incidents = WorkIncident.objects.filter(company=company_name)

    return render(request, 'incident/incident_list.html', {'incidents': incidents})


