
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class WorkIncident(models.Model):
    INCIDENT_TYPES = [
        ('accident', 'Accident'),
        ('near_miss', 'Near Miss'),
        ('injury', 'Injury'),
        ('property_damage', 'Property Damage'),
        ('other', 'Other'),
    ]

    SEVERITY_LEVELS = [
        ('minor', 'Minor'),
        ('moderate', 'Moderate'),
        ('severe', 'Severe'),
    ]

    reported_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_incidents')
    company = models.CharField(max_length=255)
    date_reported = models.DateTimeField(default=timezone.now)
    incident_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    incident_type = models.CharField(max_length=20, choices=INCIDENT_TYPES)
    description = models.TextField()
    severity = models.CharField(max_length=10, choices=SEVERITY_LEVELS)
    witnesses = models.ManyToManyField(User, related_name='witnessed_incidents', blank=True)
    action_taken = models.TextField(blank=True, null=True)
    is_resolved = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Work Incident'
        verbose_name_plural = 'Work Incidents'

    def __str__(self):
        return f"{self.get_incident_type_display()} reported by {self.reported_by} on {self.incident_date.strftime('%Y-%m-%d')}"


