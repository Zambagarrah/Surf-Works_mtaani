from django.contrib.auth.models import AbstractUser
from django.db import models

# 🎭 Custom user class: Handles EMPLOYER vs EMPLOYEE roles


class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('EMPLOYER', 'Employer'),
        ('EMPLOYEE', 'Employee'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    phone_number = models.CharField(max_length=15)
    mpesa_number = models.CharField(max_length=15)
    kra_pin = models.CharField(max_length=50, blank=True)
    county = models.CharField(max_length=50)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.username} - {self.role}"

# Helper function to structure document paths by user ID
def user_document_path(instance, filename):
    return f"documents/user_{instance.user.id}/{filename}"

# 📄 Model to handle file uploads for KRA, ID, Certifications


class Document(models.Model):
    DOC_TYPES = [
        ('ID', 'National ID'),
        ('KRA', 'KRA Certificate'),
        ('CERT', 'Professional Certification'),
        ('CV', 'Curriculum Vitae'),
    ]

    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    doc_type = models.CharField(max_length=10, choices=DOC_TYPES)
    file = models.FileField(upload_to=user_document_path)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.doc_type} | {self.user.username}"
