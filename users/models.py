

from django.db import models
from django.contrib.auth.models import User
from contractors.models import Contractor

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    mobile_phone = models.CharField(max_length=15, blank=True, null=True)
    company = models.ForeignKey(Contractor, on_delete=models.SET_NULL, null=True, blank=True)

    

class contractor(models.Model):
    company_name = models.CharField(max_length=255)
    is_archived = models.BooleanField(default=False)

    def __str__(self):
        return self.company_name






