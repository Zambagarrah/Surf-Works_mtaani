from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_choice, name='register_choice'),
    path('register/employer/', views.register_employer, name='register_employer'),
    path('register/employee/', views.register_employee, name='register_employee'),
]
