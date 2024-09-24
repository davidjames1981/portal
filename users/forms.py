from django import forms
from contractors.models import Contractor
from django.contrib.auth.models import User




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, required=False)
    password_confirm = forms.CharField(widget=forms.PasswordInput, required=False)
    mobile_phone = forms.CharField(max_length=15, required=True)
    company = forms.ModelChoiceField(queryset=Contractor.objects.filter(is_archived=False), required=False)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'is_active', 'password', 'password_confirm', 'mobile_phone', 'company']
