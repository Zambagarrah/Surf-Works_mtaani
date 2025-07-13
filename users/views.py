from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import EmployerRegistrationForm, EmployeeRegistrationForm, DocumentUploadForm
from .models import CustomUser

# 👥 Choose user role
def register_choice(request):
    return render(request, 'users/register_choice.html')

# 🧑 Employer registration flow
def register_employer(request):
    if request.method == 'POST':
        form = EmployerRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.role = 'EMPLOYER'
            user.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to appropriate employer page
    else:
        form = EmployerRegistrationForm()
    return render(request, 'users/register_employer.html', {'form': form})

# 👷 Employee registration flow
def register_employee(request):
    if request.method == 'POST':
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.role = 'EMPLOYEE'
            user.save()
            login(request, user)
            return redirect('dashboard')  # Redirect to appropriate employee page
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'users/register_employee.html', {'form': form})
