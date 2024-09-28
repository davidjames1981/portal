from django.shortcuts import render

def incident_home(request):
    return render(request, 'incident/incident.html')
