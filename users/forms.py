from django import forms
from .models import CustomUser, Document

# 👤 Form for employer registration
class EmployerRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'phone_number', 'mpesa_number',
            'kra_pin', 'county', 'password'
        ]

# 👷 Form for employee registration
class EmployeeRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = CustomUser
        fields = [
            'username', 'email', 'phone_number', 'mpesa_number',
            'county', 'password'
        ]

# 📎 Form for uploading a single document
class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ['doc_type', 'file']
