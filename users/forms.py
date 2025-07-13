from django import forms
from .models import CustomUser, Document

class EmployerRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'mpesa_number', 'kra_pin', 'county', 'password']

    password = forms.CharField(widget=forms.PasswordInput())

class EmployeeRegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone_number', 'mpesa_number', 'county', 'password']

    password = forms.CharField(widget=forms.PasswordInput())

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['doc_type', 'file']
