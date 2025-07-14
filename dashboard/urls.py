from django.urls import path
from . import views

urlpatterns = [
    path('employer/', views.employer_dashboard, name='employer_dashboard'),
    path('employee/', views.employee_dashboard, name='employee_dashboard'),
]
