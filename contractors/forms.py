from django import forms
from .models import Contractor

class ContractorForm(forms.ModelForm):
    class Meta:
        model = Contractor
        fields = ['company_name', 'contact_name', 'contact_email', 'contact_phone']




