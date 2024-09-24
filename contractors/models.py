from django.db import models


class Contractor(models.Model):
    company_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    is_archived = models.BooleanField(default=False)  # To handle archiving

    def __str__(self):
        return self.company_name
    

